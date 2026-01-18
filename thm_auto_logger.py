import os
import subprocess
from datetime import datetime

BASE_DIR = os.getcwd()

def safe_filename(name):
    return name.replace(" ", "_").replace("/", "_")

def create_room_doc(category, room_name, concepts, tools, notes):
    category_path = os.path.join(BASE_DIR, category)

    if not os.path.exists(category_path):
        os.makedirs(category_path)

    filename = safe_filename(room_name) + ".md"
    file_path = os.path.join(category_path, filename)

    content = f"""# TryHackMe Room: {room_name}

**Category:** {category}  
**Completed On:** {datetime.now().strftime('%d %B %Y')}

---

## Concepts Learned
{concepts}

---

## Tools Used
{tools}

---

## Key Takeaways
{notes}

---

⚠️ *This documentation focuses on learning outcomes. No flags or solutions are shared.*
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path

def git_commit_push(room_name):
    subprocess.run(["git", "add", "."])
    subprocess.run([
        "git",
        "commit",
        "-m",
        f"Completed TryHackMe Room: {room_name}"
    ])
    subprocess.run(["git", "push"])

def main():
    print("\n=== TryHackMe Auto Logger ===\n")

    room_name = input("Room Name: ").strip()
    category = input("Category (BlueTeam / RedTeam / Networking): ").strip()
    concepts = input("Concepts Learned (bullet points allowed):\n")
    tools = input("Tools Used:\n")
    notes = input("Key Takeaways:\n")

    file_path = create_room_doc(category, room_name, concepts, tools, notes)
    print(f"\n✔ Documentation created: {file_path}")

    push = input("Push to GitHub now? (y/n): ").lower()
    if push == "y":
        git_commit_push(room_name)
        print("✔ Changes pushed to GitHub successfully!")

if __name__ == "__main__":
    main()
