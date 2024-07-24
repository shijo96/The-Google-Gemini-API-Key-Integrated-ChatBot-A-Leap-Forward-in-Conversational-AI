# Specific topic realted ChatBot

# import pathlib
# import textwrap
# import google.generativeai as genai
# import os
# from flask import Flask, request, jsonify, render_template
# from IPython.display import display, Markdown

# app = Flask(__name__)

# # Google Gemini API Key
# GOOGLE_API_KEY = 'AIzaSyAzL1VBdXYPWO1CCWcx7-tDiEd2-zgJvlQ'

# genai.configure(api_key=GOOGLE_API_KEY)

# model = None
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         break

# def to_markdown(text):
#     text = text.replace('*', ' ')
#     return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# def generate_gemini_response(prompt):
#     # Add context to the prompt to focus on medicinal plants and Ayurveda
#     context_prompt = f"This conversation is about medicinal plants and Ayurveda. {prompt}"
#     response = model.generate_content(context_prompt)
#     return response.text

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json.get('message')
#     # Optional: Filter user input to check for relevant topics
#     if not ('plant' in user_message.lower() or 'ayurveda' in user_message.lower() or 'medicine' in user_message.lower()):
#         return jsonify({'response': 'Please ask questions related to medicinal plants and Ayurveda.'})
#     gemini_response = generate_gemini_response(user_message)
#     return jsonify({'response': gemini_response})

# if __name__ == '__main__':
#     app.run(debug=True)




# ChatBot - All About


import pathlib
import textwrap
import google.generativeai as genai
import os
from flask import Flask, request, jsonify, render_template
from IPython.display import display, Markdown

app = Flask(__name__)

GOOGLE_API_KEY = 'AIzaSyAzL1VBdXYPWO1CCWcx7-tDiEd2-zgJvlQ'

genai.configure(api_key=GOOGLE_API_KEY)

model = None
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
        model = genai.GenerativeModel('gemini-1.5-flash')
        break

def to_markdown(text):
    text = text.replace('*', ' ')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def generate_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    gemini_response = generate_gemini_response(user_message)
    return jsonify({'response': gemini_response})

if __name__ == '__main__':
    app.run(debug=True)
