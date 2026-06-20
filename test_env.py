from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

response = llm.invoke("Say hello")

print(response.content)
print(os.getenv("GOOGLE_API_KEY")[:10])
print(llm.invoke("What is LangGraph?").content)