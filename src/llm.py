from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

def generate_answer(prompt: str, max_length=100) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_length=max_length, do_sample=True, top_k=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
