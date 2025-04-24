# Multimodal-Assistant

A multimodal assistant that understands both images and text, capable of answering questions about visual content in natural language. This project integrates image captioning and language generation models into a seamless pipeline with a real-time Gradio interface.

🔍 Features
📸 Image Understanding: Generate natural language captions from uploaded images using BLIP

🧾 Question Answering: Answer user questions about the image context using a GPT-2 language model

🔀 Prompt Fusion: Combine image caption and user query into a single structured prompt for response generation

🌐 Web UI: Gradio-based interface for real-time interaction (image upload + question input)

⚙️ Optional support for switching to larger LLMs like Mistral, Falcon, or LLaMA

🚀 Demo
Run locally:

bash
Sao chép
Chỉnh sửa
git clone https://github.com/yourusername/multimodal-ai-assistant.git
cd multimodal-ai-assistant
pip install -r requirements.txt
python app.py
Then open your browser: http://localhost:7860

🧩 Tech Stack
Language: Python

Models: BLIP (image captioning), GPT-2 (language generation)

Libraries: Hugging Face Transformers, PyTorch, Gradio

Deployment: Local Gradio app (can be extended to Hugging Face Spaces)

📁 Folder Structure
bash
Sao chép
Chỉnh sửa
multimodal-ai-assistant/
│
├── app.py              # Gradio UI
├── main.py             # Core pipeline logic
├── requirements.txt
├── /src/
│   ├── vision.py       # Image captioning logic (BLIP)
│   └── llm.py          # Language model response (GPT-2)
└── /data/              # Sample images (optional)
📌 Future Improvements
 Support Vietnamese language (prompt translation or Vietnamese LLM)

 Integrate BLIP-2 for VQA

 Add object detection for localized queries

 Save user interaction history

🙋 Author
Nguyễn Mạnh Dũng
