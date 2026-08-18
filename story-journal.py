import os

from utils.generatestory import generateStory
from utils.journalutils import extract_story_info, storeJournals

MODEL = "llama3.2:1b"
if not os.path.exists("./journals"):
    os.makedirs("./journals")


with open("./utils/prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read().strip()

response = generateStory(model=MODEL, prompt=prompt)
title, timestamp = extract_story_info(response)

storeJournals(heading=title, timestamp=timestamp, content=response)
