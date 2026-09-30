from fastapi import FastAPI
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = FastAPI()

client = genai.Client()


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/ask")
def ask_ai(question: str):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )

        return {
            "answer": response.text
        }

    except Exception as e:
        print("ERROR:", e)
        return {
                "answer": str(e)
        }
      
    
    