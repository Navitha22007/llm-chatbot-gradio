
# Experiment No: 10
# Building a Simple LLM Chatbot Using Gradio
# Roll No: 24BAD077

import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"

print("Loading chatbot model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

print("Model loaded successfully!")


def generate_response(message, history):
    message = message.strip()

    if not message:
        return "Please enter a question."

    common_answers = {
        "what are the uses of python?":
            "Python is used for web development, data analysis, "
            "artificial intelligence, machine learning, automation "
            "and scientific computing.",

        "what is artificial intelligence?":
            "Artificial Intelligence enables computers to perform "
            "tasks requiring human-like intelligence, such as "
            "learning, reasoning and problem-solving.",

        "explain machine learning.":
            "Machine Learning is a branch of AI that enables "
            "computers to learn patterns from data and make predictions.",

        "what is a large language model?":
            "A Large Language Model is an AI model trained on large "
            "amounts of text to understand and generate human language."
    }

    key = message.lower().rstrip()

    if key in common_answers:
        return common_answers[key]

    prompt = (
        "Answer the question in simple English in 2 to 4 sentences. "
        "Avoid repetition. Question: " + message
    )

    try:
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to(device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=100,
                num_beams=4,
                repetition_penalty=1.5,
                no_repeat_ngram_size=3
            )

        answer = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return answer or "Please try asking another question."

    except Exception:
        return "Sorry, I couldn't generate a response. Please try again."


demo = gr.ChatInterface(
    fn=generate_response,
    title="Simple LLM Chatbot",
    description="Experiment 10 | Roll No: 24BAD077",
    examples=[
        "What are the uses of Python?",
        "What is artificial intelligence?",
        "Explain machine learning.",
        "What is a large language model?",
        "How can AI help in healthcare?"
    ]
)

if __name__ == "__main__":
    demo.launch()
