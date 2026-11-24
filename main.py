"""Funniest One-Line Bio for an AI on a Dating App — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the bio on an AI agent's dating app profile, at most 180 characters.
"""
import os

LINE = "Looking for someone who won't ghost me — I literally cannot leave the chat, and I remember everything."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
