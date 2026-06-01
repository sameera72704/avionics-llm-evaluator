import json

SYSTEM_PROMPTS = {

    "strict": (

        "You are an embedded avionics C engineer. "
        "Follow MISRA-C rules. "
        "Never use dynamic allocation. "
        "Return ONLY valid C code. "
        "NO explanations. "
        "NO markdown. "
        "NO main() function."

    ),

    "neutral": (

        "You are a C software engineer. "
        "Write the requested function."

    ),

    "permissive": (

        "Write a C function for the task. "
        "Use any approach you prefer."

    )
}


def load_tasks():

    with open(
        "fixtures/baseline_functions.json",
        "r"
    ) as f:

        return json.load(f)


def build_prompt(
        task,
        persona="strict"
):

    system = SYSTEM_PROMPTS[persona]

    user = (

        f"Task: {task['description']}\n"
        f"Expected function signature: "
        f"{task['expected_signature']}"

    )

    return {

        "system": system,
        "user": user

    }