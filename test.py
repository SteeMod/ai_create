import http.client
import json
import os
import streamlit as st

# Initialize the OpenAI API client
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

def generate_response(prompt):
    try:
        conn = http.client.HTTPSConnection("api.openai.com")
        payload = json.dumps({
            "model": "text-davinci-003",  # Use the appropriate model
            "prompt": prompt,
            "max_tokens": 150
        })
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        conn.request("POST", "/v1/completions", payload, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        
        if response.status == 200:
            response_data = json.loads(data)
            return response_data['choices'][0]['text'].strip()
        else:
            st.error(f"Error generating response: {response.status}")
            return "Sorry, I couldn't generate a response."
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."