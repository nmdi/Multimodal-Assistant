import gradio as gr
from src.vision import describe_image
from src.llm import generate_answer

def process(image, question):
    caption = describe_image(image)
    prompt = f"Image description: {caption}. Question: {question} → Answer:"
    answer = generate_answer(prompt)
    return caption, answer

demo = gr.Interface(
    fn=process,
    inputs=[
        gr.Image(type="filepath", label="Upload Image"),
        gr.Textbox(lines=2, placeholder="What do you want to ask about the image?", label="Your Question"),
    ],
    outputs=[
        gr.Textbox(label="Image Caption"),
        gr.Textbox(label="Answer"),
    ],
    title="🧠 Multimodal Assistant",
    description="Upload an image and ask a question about it. The assistant will describe and answer your query.",
)

if __name__ == "__main__":
    demo.launch()
