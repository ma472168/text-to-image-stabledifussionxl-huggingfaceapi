import gradio as gr
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# 1. Cargar API Key desde archivo .env (no t robes la mia porfi :( )
load_dotenv()
token = os.getenv("HF_TOKEN")

if not token:
    raise ValueError("HF_TOKEN no encontrado en las variables de entorno.")

# 2. Configurar el cliente de Hugging Face Inference
# Usamos Stable Diffusion XL Base 1.0 como modelo
client = InferenceClient(model="stabilityai/stable-diffusion-xl-base-1.0", token=token)

def generar_imagen(prompt):
    if not prompt:
        return None
    
    print(f"Generando imagen para el prompt: {prompt}")
    try:
        image = client.text_to_image(prompt)
        return image
    except Exception as e:
        print(f"Error al generar la imagen: {e}")
        return None
    
# 3. Inferfaz de usuario con Gradio
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Generador de Imágenes con Stable Diffusion XL")
    gr.Markdown("Introduce un prompt y genera una imagen usando Stable Diffusion XL Base 1.0.")
    
    with gr.Row():
        with gr.Column():
            texto_input = gr.Textbox(
                label="Prompt de Texto",
                placeholder="Describe la imagen que quieres generar...",
                lines=2
            )
            boton_generar = gr.Button("Generar Imagen", variant="primary")

            with gr.Column():
                imagen_output = gr.Image(label="Resultado")
    
    boton_generar.click(fn=generar_imagen, inputs=texto_input, outputs=imagen_output)

if __name__ == "__main__":
    demo.launch()