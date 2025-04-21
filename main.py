from .src.vision import describe_image
from .src.llm import generate_answer

image_path = "data/dog.jpg"
user_question = "What is happening in this image?"

# 1. Tạo caption
caption = describe_image(image_path)
print(f"[🖼️ Caption]: {caption}")

# 2. Prompt tiếng Anh
full_prompt = f"Image description: {caption}. Question: {user_question} → Answer:"
answer = generate_answer(full_prompt)

print(f"[🤖 Answer]: {answer}")
