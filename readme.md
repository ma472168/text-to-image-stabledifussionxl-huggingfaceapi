
# 🎨Text-to-Image Application powered by Stable Diffusion XL & Hugging Face API	

## 📝 Overview

This application allows users to generate high-quality images from text descriptions (prompts) in seconds. Instead of requiring a powerful GPU locally, it securely connects to the **Hugging Face Inference API** to run the **Stable Diffusion XL** model in the cloud.

## ✨ Key Features

* **State-of-the-Art Model:** Uses `stabilityai/stable-diffusion-xl-base-1.0` for high-fidelity generation.
* **Fast Inference:** Generates images in seconds using cloud acceleration.
* **Secure Architecture:** Uses Environment Variables (`.env`) to keep API keys safe and out of version control.
* **Simple UI:** Built with Gradio for an intuitive experience.

## 📸 Demo

![Demo Screenshot](demo.png)

## 🛠️ Tech Stack

* **Language:** Python 3
* **Cloud API:** Hugging Face Serverless Inference
* **Security:** `python-dotenv` for key management
* **GUI:** Gradio

## 🚀 Installation & Setup

Since this project uses sensitive API keys, follow these steps carefully to set it up locally.
no t robes mi api we :(

### 1. Clone the repository
```bash
git clone <https://github.com/ma472168/text-to-image-stabledifussionxl-huggingfaceapi.git>
cd generador-arte-ai
```

### 2. Create a Virtual Environment


```bash
python -m venv venv
.\venv\Scripts\activate```
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. 🔐 API Configuration (Crucial Step)

You need a Hugging Face Access Token to run this app.

1.  Create a file named `.env` in the root folder of the project.
    
2.  Get your free token at [Hugging Face Settings](https://huggingface.co/settings/tokens).
    
3.  Add the following line to the `.env` file:
   
    ```Plaintext
    HF_TOKEN=hf_your_token_starts_with_hf_...
    ```
    

## ⚡ Usage

Run the application:


```bash
python app.py
```

Open your browser at `http://127.0.0.1:7860`.
