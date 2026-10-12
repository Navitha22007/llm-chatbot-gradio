# Simple LLM Chatbot Using Gradio

## Experiment No. 10

**Title:** Building a Simple LLM Chatbot Using Streamlit/Gradio

**Roll Number:** 24BAD077

## Objective

To develop a simple chatbot using a pretrained Large Language Model (LLM) and an interactive web interface.

## Technologies Used

- Python
- Hugging Face Transformers
- FLAN-T5 pretrained language model
- Gradio
- PyTorch
- Google Colab

## Description

This project implements a simple conversational chatbot using the FLAN-T5 language model. The model generates responses to user questions, while Gradio provides an interactive web interface.

Predefined responses are also included for selected common questions to provide consistent answers.

## Features

- Interactive chatbot interface
- Pretrained language model integration
- Responses to user questions
- Example prompts for testing
- Repetition control during text generation

## Project Structure

```text
llm-chatbot-gradio/
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── model_loading.png
    ├── chatbot_interface.png
    └── chatbot_response.png
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Execution

Run the application:

```bash
python app.py
```

The application opens a Gradio interface in the browser. Enter a question in the message box to interact with the chatbot.

The first run downloads the pretrained model, so an internet connection is required.

## Sample Questions

1. What are the uses of Python?
2. What is artificial intelligence?
3. Explain machine learning.
4. What is a large language model?
5. How can AI help in healthcare?

## Expected Result

The chatbot accepts user questions and displays responses through an interactive Gradio web interface.

## Limitations

FLAN-T5 is a relatively small language model and may produce inaccurate or incomplete responses. Its answers should be verified before use.

## Conclusion

A simple LLM chatbot was implemented using Python, Hugging Face Transformers, PyTorch and Gradio. The application demonstrates pretrained language model integration and interactive text generation.