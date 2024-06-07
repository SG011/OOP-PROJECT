import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyA7dtVBKkqzZF7aHcSpt9hBtxxqC4htOmQ"

user_text1 = """
Give me the sentiment of this sentence:
"I hate this movie"
"""

user_text2 = """
Give me hindi translation of this sentence:
"I hate this movie"
"""

user_text3 = """
Detect the language of this sentence:
"I hate this movie"
"""

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content(user_text3)
results = response.text
print(results)