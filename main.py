from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 1. Initializing Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",  # or "gemini-1.5-flash"
    temperature=0.7,
    google_api_key=GEMINI_API_KEY
)

# 2. First step: generate a title
title_prompt = ChatPromptTemplate.from_template(
    "Give me a catchy YouTube title about {topic}."
)
title_chain = title_prompt | llm | StrOutputParser()

# 3. Second step: write a script based on the title
script_prompt = ChatPromptTemplate.from_template(
    "Write a YouTube video script for the title: {title}."
)
script_chain = script_prompt | llm

chain = title_chain | script_chain

def generate_script(topic):
    #Generating a YT script from topic
    script = chain.invoke({'topic':topic})
    return script.content



