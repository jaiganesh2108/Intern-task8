<h1>Rule-Based Chatbot!</h1>

## Overview:

This is a simple rule-based chatbot implemented in Python. The chatbot responds to user inputs based on predefined regular expression (regex) patterns, providing a friendly and interactive conversational experience. It uses basic natural language processing (NLP) techniques to match user inputs and select appropriate responses.

## Features:

Interactive Conversation: Engages users with varied, humanized responses.
Regex Pattern Matching: Matches user inputs against predefined patterns for response selection.
Error Handling: Gracefully handles unexpected inputs and interruptions (e.g., Ctrl+C).
Extensible Rules: Easily add new patterns and responses to enhance functionality.
Command-Line Interface: Simple input/output loop for real-time chatting.

---

## Requirements:

Python 3.6 or higher

---

## Standard Python libraries:
- re (for regex) and random (for response selection)

---

## Installation:

## Clone or Download the Repository:

```
git clone https://github.com/jaiganesh2108/Intern-task8.git
cd rule-based-chatbot
```

Ensure Python is Installed: Verify Python installation by running:

- python --version
- If Python is not installed, download and install it from python.org.

---

## No Additional Dependencies: The script uses only standard Python libraries (re and random), so no additional packages are required.

---

## Usage:

Run the Script: Navigate to the directory containing the script (chatbot.py) and run:
```
python chatbot.py
```


Interact with the Chatbot:

The chatbot will display a welcome message:
```
Bot: Hi! I'm J.A.R.V.I.S, your rule-based chatbot. Type 'exit' to end our chat.
You: hello
Bot: Hey, what's up?
You: how are you
Bot: I'm a bot, so I'm always 100%!
You: what is your name
Bot: I'm J.A.R.V.I.S, your friendly chatbot!
You: thanks
Bot: You're welcome!
You: something random
Bot: Hmm, I'm not sure I understand. Could you rephrase that?
You: bye
Bot: Goodbye! Thanks for chatting!
```
