import google.generativeai as genai
from django.conf import settings

def initialize_gemini_client():
    genai.configure(api_key=settings.GOOGLE_API_KEY)
    return genai

def get_gemini_response(prompt):
    genai_client = initialize_gemini_client()
    model = genai_client.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
