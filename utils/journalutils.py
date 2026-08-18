import re


def storeJournals(heading: str, timestamp: str, content: str):
    headingStripped = "-".join(heading.split()).lower()
    # Remove any invalid filename characters
    heading_clean = re.sub(r'[\\/*?:"<>|]', "", headingStripped)
    
    if timestamp:
        timestamp_clean = re.sub(r'[\\/*?:"<>|]', "", "-".join(timestamp.split()).lower())
        filename = f"{heading_clean}-{timestamp_clean}.md"
    else:
        filename = f"{heading_clean}.md"

    path = f"./journals/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Journal stored at {path}")
    return path


def extract_story_info(story: str):
    # First H1 heading
    title_match = re.search(r"^#\s+\*\*(.*?)\*\*", story, re.MULTILINE)

    title = title_match.group(1).strip() if title_match else "Untitled"

    # ONLY the first timestamp/date
    timestamp_match = re.search(r"^\*\*(?:📅|🕐)\s*(.*?)\*\*", story, re.MULTILINE)

    timestamp = timestamp_match.group(1).strip() if timestamp_match else ""

    return title, timestamp
