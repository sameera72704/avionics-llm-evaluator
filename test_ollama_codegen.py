import ollama

from src.prompts.prompt_builder import *

tasks = load_tasks()

prompt = build_prompt(
    tasks[0],
    "strict"
)

response = ollama.chat(

    model="mistral",

    messages=[

        {
            "role":"system",
            "content":prompt["system"]
        },

        {
            "role":"user",
            "content":prompt["user"]
        }
    ]
)

print(
    response["message"]["content"]
)