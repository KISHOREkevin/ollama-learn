def storeJournals(heading: str, timestamp: str, content: str):
    headingStripped = heading.split(" ").join("-").lower()
    path = f"./journals/{headingStripped}-{timestamp}.md"
    with open(path, "w") as f:
        f.write(content.strip())
    print(f"Jpunal stored at {path}")
