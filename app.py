import os
import time
import google.generativeai as genai
import gradio as gr
from functools import lru_cache

# Configure the Generative AI model
genai.configure(api_key="API_Key")

# IMPORTANT CHANGE: Using 'gemini-1.5-flash' as requested.
# This model is generally available and good for quick responses.
model = genai.GenerativeModel('gemini-1.5-flash') 

@lru_cache(maxsize=50)
def qa_chatbot(query):
    try:
        # Keep the sleep duration as it helps with rate limiting for free tiers
        time.sleep(2.5) 
        response = model.generate_content(
            f"Act as QA expert. Be concise. Question: {query}"
        )
        return response.text
    except Exception as e:
        # Updated error message for more general API issues
        return f"An API error occurred: {str(e)}. Please check your model name, API key, or Google Cloud project configuration."

# Gradio Interface setup
gr.Interface(
    fn=qa_chatbot,
    inputs="textbox",
    outputs="text",
    title="QA Assistant",
    description="Ask a question and get a concise answer from the AI QA expert."
).launch()
