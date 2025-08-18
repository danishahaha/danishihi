# wait_for_nisha.py

import time
import sys
import os

# Animation frames (a heart that "beats")
HEART_FRAMES = [
r"""
   **     **
  ****   ****
  ***********
   *********
    *******
     *****
      ***
       *
""",
r"""
    ***   ***
   ***** *****
   ***********
    *********
     *******
      *****
       ***
        *
"""
]

# Message for Nisha
message_lines = [
    "Hi Nisha,",
    "",
    "I know you’re not ready for a relationship right now,",
    "and I respect that with all my heart.",
    "",
    "I just want you to know this:",
    "I’ll be here, waiting patiently for the day",
    "when you’re ready to take that step.",
    "",
    "Your flaws, imperfections, and everything in between,",
    "they don’t push me away — they make you real.",
    "",
    "Take all the time you need, Nisha.",
    "I’ll always be here.",
    "",
    "From,",
    "Me"
]

filename = "note_for_nisha.txt"

# Typewriter effect
def typewriter(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

# Animation
def pulse_heart(beats=5, pause=0.5):
    for i in range(beats):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(HEART_FRAMES[i % len(HEART_FRAMES)])
        time.sleep(pause)

# Main program
pulse_heart(beats=6)
os.system('cls' if os.name == 'nt' else 'clear')

for line in message_lines:
    typewriter(line, speed=0.04)

# Save message to file
with open(filename, "w", encoding="utf-8") as f:
    f.write("\n".join(message_lines))

print(f"\nMessage saved as '{filename}'. You can send this file to Nisha.")
