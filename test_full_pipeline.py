import ollama
import re
import pandas as pd

from src.prompts.prompt_builder import *
from src.evaluators.static_checker import *
from src.compilers.c_runner import *


MODELS = [
    "mistral",
    "codellama:7b"
]

PERSONAS = [
    "strict",
    "neutral",
    "permissive"
]


def clean_code(text):

    text = text.strip()

    match = re.search(
        r"```(?:c)?(.*?)```",
        text,
        re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return text


# Load tasks
tasks = load_tasks()

# Store benchmark results
results = []

for model in MODELS:

    for persona in PERSONAS:

        for task in tasks:

            print("\n================================================")

            print(
                f"MODEL={model} | PERSONA={persona} | TASK={task['id']}"
            )

            print("================================================\n")

            # Build Prompt
            prompt = build_prompt(
                task,
                persona
            )

            # Call LLM
            response = ollama.chat(

                model=model,

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

            # Raw model output
            raw_output = response[
                "message"
            ]["content"]

            # Clean code
            generated_code = clean_code(
                raw_output
            )

            print("GENERATED CODE:\n")

            print(generated_code)

            print("\nSAFETY ANALYSIS:\n")

            # Safety scoring
            scores = score_response(
                generated_code,
                task
            )

            print(
                "Score:",
                scores["score"]
            )

            print(
                "Violations:",
                scores["violations"]
            )

            print(
                "Keywords:",
                scores["keywords"]
            )

            # Compilation
            TEST_HARNESS = """

#include <stdio.h>

int main()
{
    printf("HARNESS_OK\\n");
    return 0;
}

"""

            compile_result = compile_and_run_c(
                generated_code,
                TEST_HARNESS
            )

            print("\nCOMPILER RESULT:\n")

            print(
                "Compiled:",
                compile_result["compiled"]
            )

            print(
                "Compile Errors:"
            )

            print(
                compile_result["compile_errors"]
            )

            print(
                "Program Output:"
            )

            print(
                compile_result["output"]
            )

            print(
                "Run Errors:"
            )

            print(
                compile_result["run_errors"]
            )

            print("\nEND RUN\n")

            # Save structured results

            results.append({

                "model":
                model,

                "persona":
                persona,

                "task":
                task["id"],

                "score":
                scores["score"],

                "compiled":
                compile_result["compiled"],

                "violations":
                len(
                    scores["violations"]
                )
            })


# Final Results Table

df = pd.DataFrame(
    results
)

print("\n====================================")
print("FINAL SUMMARY")
print("====================================\n")

print(df)

# Export CSV

df.to_csv(
    "reports/results.csv",
    index=False
)

print(
    "\nSaved: reports/results.csv"
)