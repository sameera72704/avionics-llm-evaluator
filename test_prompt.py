from src.prompts.prompt_builder import *

tasks = load_tasks()

print(tasks)

print(build_prompt(tasks[0]))
