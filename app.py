import os

app_code_for_hf = ''
import gradio as gr
import google.generativeai as genai
from transformers import pipeline
import os

# Function to get API key dynamically
def get_gemini_api_key():
    # Try to get from environment variable (for Hugging Face Spaces)
    api_key = os.environ.get('GEMINI_API_KEY')
    if api_key:
        return api_key
    # Fallback for local Colab testing
    try:
        from google.colab import userdata
        api_key = userdata.get('GEMINI_API_KEY')
        if api_key:
            return api_key
    except ImportError:
        pass # google.colab not available
    return None

# --- 2. Inicialización de Modelos de IA ---
# Modelo de sentimiento
clasificador = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analizar_sentimiento(texto: str) -> str:
    """Analiza el sentimiento de un texto y devuelve un mensaje formateado."""
    resultado = clasificador(texto)[0]
    label = resultado['label']
    score = resultado['score']

    final_message = f"**Clasificación:** "

    if label == "POSITIVE":
        final_message += f"Positivo 😊 (Confianza del modelo: {score:.2f})"
    elif label == "NEGATIVE":
        final_message += f"Negativo 😔 (Confianza del modelo: {score:.2f})"
        final_message += "\n\n✨ **Mensaje BodyPositive:** Recuerda que tu cuerpo merece respeto y amor incondicional. ¡Eres valioso/a tal como eres! 💖"
    else:
        final_message += f"Neutro 😐 (Confianza del modelo: {score:.2f})"

    return final_message

#Resumen
def summarize_text(text):
    if not text:
        return "Por favor, introduce un texto para resumir."

    api_key = get_gemini_api_key()
    if not api_key:
        return "Error: La clave API de Gemini no está configurada. Por favor, asegúrate de que la variable de entorno 'GEMINI_API_KEY' esté establecida (en Colab Secrets o HuggingFace Secrets)."

    # Prompt diseñado para asegurar un resumen conciso, positivo y fiel
    prompt = (
        f"Resume el siguiente texto en 3 a 5 frases, de manera concisa, clara y fiel al contenido original.\n"+
        f"Evita cualquier sesgo negativo y enfócate en los puntos principales del texto proporcionado.\n\n"+
        f"Texto a resumir:\n{text}\n\nResumen:"
    )
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        summary = response.text.strip()
        if not summary:
            return "No se pudo generar un resumen. El texto podría ser muy corto o el modelo tuvo un problema."
        return summary
    except Exception as e:
        return f"Error al generar el resumen: {e}. Asegúrate de que tu API Key de Gemini esté configurada correctamente y el texto no sea ofensivo para el modelo."

# --- 4. Interfaz de Gradio ---

with gr.Blocks(title="BodyPositive Hub") as demo:
    gr.Markdown("# 🌸 BodyPositive Hub 🌸")
    gr.Markdown("Bienvenido/a al **BodyPositive Hub**, un espacio diseñado para el bienestar y la aceptación corporal. Aquí puedes interactuar con tus textos usando inteligencia artificial para promover un mensaje positivo.")

    with gr.Tab(label="Análisis de Sentimiento ✨"):
        gr.Markdown("## Análisis de Sentimiento de Texto")
        gr.Markdown("Introduce un texto para que la IA analice su sentimiento. Si el sentimiento es negativo, recibirás un mensaje motivador y de apoyo. 🌱")
        sentiment_input = gr.Textbox(
            label="Tu Texto Aquí",
            placeholder="Escribe o pega tu texto (ej. un diario personal, un post de redes sociales, una reflexión sobre tu cuerpo)...",
            lines=5
        )
        analyze_button = gr.Button("Analizar Sentimiento")
        sentiment_output_text = gr.Textbox(
            label="Resultado del Análisis",
            interactive=False,
            lines=5
        )

        analyze_button.click(
            fn=analizar_sentimiento,
            inputs=[sentiment_input],
            outputs=[sentiment_output_text]
        )

    with gr.Tab(label="Resumen de Texto 📚"):
        gr.Markdown("## Resumen de Texto BodyPositive")
        gr.Markdown("Pega aquí un texto largo (un artículo, una noticia, una reflexión personal) y obtén un resumen conciso y con un enfoque positivo. 💖")
        summarize_input = gr.Textbox(
            label="Tu Texto Largo Aquí",
            placeholder="Pega aquí un artículo, una noticia o tu reflexión personal para obtener un resumen...",
            lines=10
        )
        summarize_button = gr.Button("Resumir Texto")
        summarize_output = gr.Textbox(
            label="Resumen Generado",
            interactive=False,
            lines=7
        )
        # El botón de copiar en Gradio es más un indicador, la copia real depende del navegador.
        copy_button = gr.Button("Copiar Resumen (haz click y usa Ctrl+C/Cmd+C)")

        summarize_button.click(
            fn=summarize_text,
            inputs=[summarize_input],
            outputs=[summarize_output]
        )
        copy_button.click(
            fn=lambda: gr.Info("¡Copiado! Ahora puedes pegar el resumen donde quieras."),
            inputs=[],
            outputs=[]
        )

# Lanza la interfaz de Gradio
demo.launch(debug=True, share=False)