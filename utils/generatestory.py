import sys

import ollama

REFUSAL_PHRASES = [
    "i cannot provide",
    "i can't provide",
    "i cannot create",
    "i can't create",
    "i cannot tell",
    "i can't tell",
    "i cannot help",
    "i can't help",
    "i'm not sure i can",
    "i am not sure i can",
    "i'm unable to",
    "i am unable to",
    "i cannot fulfill",
    "i can't fulfill",
    "i'm unable",
    "i am unable",
    "cannot fulfill your request",
    "can't fulfill your request",
    "i must adhere to certain guidelines",
    "guidelines and standards",
    "suggest some alternative approaches",
    "please let me know which option",
    "is there anything else i can help",
]


def is_refusal(response: str) -> bool:
    text = response.lower().strip()

    return any(phrase in text for phrase in REFUSAL_PHRASES)


def generateStory(model: str, prompt: str, retries: int = 3):

    try:
        for attempt in range(1, retries + 1):
            print(f"Generating story... (attempt {attempt}/{retries})")

            response = ollama.generate(model=model, prompt=prompt)

            result = response.get("response", "").strip()

            if not result:
                print("Empty response.")
                continue

            if is_refusal(result):
                print("Model refused. Retrying...")
                continue

            print("Story generated!")

            return result

        print("Failed to generate a story after multiple attempts.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
