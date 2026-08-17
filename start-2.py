import ollama
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown

with open("crime-teller.txt", "r", encoding="utf-8") as file:
    systemContents = file.read()

console = Console()

quit_commands = ["exit", "quit", "break", "close"]

ollama.create(
    from_="llama3.2:1b",
    model="kevin",
    system=systemContents,
    parameters={"temperature": 1.5},
)

try:
    while True:
        prompt = input("\nYou: ")

        if prompt.lower() in quit_commands:
            break

        response = ollama.generate(model="kevin", prompt=prompt, stream=True)

        result = ""

        console.print("\nKevin:")

        with Live(Markdown(""), console=console, refresh_per_second=15) as live:
            for chunk in response:
                result += chunk["response"]
                live.update(Markdown(result))

finally:
    ollama.delete("kevin")
