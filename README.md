---
title: BodyPositiveHub
emoji: 🐠
colorFrom: yellow
colorTo: indigo
sdk: gradio
sdk_version: 6.14.0
python_version: '3.13'
app_file: app.py
pinned: false
short_description: Analiza sentimientos y promueve el body positive
---
# 🌸 BodyPositive Hub 🌸
# Link a la app desplegada en HuggingFace: https://huggingface.co/spaces/vhdezc/BodyPositiveHub 

## Descripción del Proyecto

**BodyPositive Hub** es una aplicación web diseñada para fomentar la aceptación corporal y la autoestima a través de herramientas de Inteligencia Artificial. Permite a los usuarios interactuar con sus textos de dos maneras principales:

1.  **Análisis de Sentimiento**: Evalúa el tono emocional de un texto ingresado por el usuario, ofreciendo mensajes motivadores si el sentimiento detectado es negativo.
2.  **Resumen de Texto**: Genera resúmenes concisos y fieles de textos largos, con un enfoque Body Positive que evita sesgos negativos.

El objetivo de esta aplicación es proporcionar un espacio accesible y amigable donde los usuarios puedan reflexionar sobre sus sentimientos y recibir apoyo, promoviendo un lenguaje claro, amoroso y constructivo.

## Características Principales

*   Interfaz intuitiva con pestañas para cada funcionalidad.
*   Análisis de sentimiento con clasificación (Positivo/Negativo) y emojis representativos.
*   Mensajes motivadores automáticos para sentimientos negativos.
*   Resumen de textos largos en 3-5 frases.
*   Funcionalidad de copiar resultados para fácil compartición.

## Tecnologías Utilizadas

*   **Framework de Interfaz**: [Gradio](https://gradio.app/) para la creación de la interfaz web con pestañas.
*   **Backend**: Python.
*   **Análisis de Sentimiento**: Modelo `distilbert-base-uncased-finetuned-sst-2-english` de [HuggingFace Transformers](https://huggingface.co/transformers).
*   **Resumen de Texto**: [Gemini API](https://ai.google.dev/) (modelo `gemini-2.5-flash`) de Google Generative AI.

## Instalación y Ejecución Local

Para ejecutar BodyPositive Hub en tu entorno local, sigue estos pasos:

### 1. Clona el repositorio (si aplica) o descarga los archivos

Si el proyecto está en un repositorio, clónalo:

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd BodyPositiveHub
```

Si no, asegúrate de tener `app.py` y `requirements.txt` en el mismo directorio.

### 2. Configura tu entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
# venv\Scripts\activate  # En Windows
```

### 3. Instala las dependencias

Instala las librerías necesarias utilizando `pip` y el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debe contener:

```
gradio
transformers
google-generativeai
```

### 4. Configura tu API Key de Gemini

Para utilizar la funcionalidad de resumen de texto, necesitas una API Key de Gemini. 

*   Obtén tu API Key desde [Google AI Studio](https://aistudio.google.com/apikey).
*   Crea un archivo llamado `.env` en la raíz de tu proyecto y añade tu clave:
    ```
    GEMINI_API_KEY="TU_API_KEY_AQUI"
    ```
    > **Nota**: Asegúrate de añadir `.env` a tu `.gitignore` para no subir tu clave a repositorios públicos.
*   Para ejecutar localmente, el código está configurado para intentar obtener la clave de `google.colab.userdata` o de `os.environ`. Si tienes problemas, puedes configurar la variable de entorno `GEMINI_API_KEY` manualmente en tu terminal antes de ejecutar la app.

### 5. Ejecuta la aplicación

```bash
python app.py
```

Esto iniciará la aplicación Gradio, y podrás acceder a ella a través de la URL local que se mostrará en tu terminal (usualmente `http://127.0.0.1:7860`).

## Despliegue en Hugging Face Spaces

BodyPositive Hub está diseñada para ser fácilmente desplegable en [Hugging Face Spaces](https://huggingface.co/spaces).

### Pasos para el Despliegue:

1.  **Crea un Nuevo Space**: Ve a [huggingface.co/new-space](https://huggingface.co/new-space).
    *   Elige un nombre para tu Space.
    *   Selecciona `Gradio` como SDK.
    *   Elige `Public` o `Private` según tu preferencia.
    *   Selecciona un hardware adecuado (CPU Basic es suficiente para empezar).

2.  **Sube los Archivos**: Sube `app.py` y `requirements.txt` a tu Space.
    *   `app.py` contendrá todo el código de la aplicación Gradio (tal como se generó para despliegue).
    *   `requirements.txt` debe contener `gradio`, `transformers`, y `google-generativeai`.

3.  **Configura el Secreto de Gemini API Key**: 
    *   En tu Hugging Face Space, ve a la pestaña `Settings`.
    *   En la sección `Repository secrets`, añade un nuevo secreto con el nombre `GEMINI_API_KEY` y tu clave API de Gemini como valor.

4.  **Espera la Construcción**: Hugging Face Spaces construirá automáticamente tu aplicación. Puedes monitorear el progreso y los logs en la pestaña `Logs`.

5.  **¡Tu App está Online!**: Una vez que la construcción sea exitosa, tu aplicación estará disponible en una URL pública (ej. `https://tu-usuario-tu-space.hf.space`).
