import re
import random

class RuleBot:
    def __init__(self):
        # regex patterns and corresponding response lists
        self.rules = {
            r"(hello|hi|hey)\b": ["Hello! Nice to see you!", "Hi there!", "Hey, what's up?", "Welcome back!"],
            r"how are you\b": ["I'm doing great, thanks for asking!", "Just chilling in the digital realm!", "I'm a bot, so I'm always 100%!"],
            r"what is your name\b": ["I'm J.A.R.V.I.S, your friendly chatbot!", "Call me J.A.R.V.I.S, nice to meet you!", "My name's J.A.R.V.I.S, what's yours?"],
            r"(bye|goodbye|exit|quit)\b": ["Goodbye! Come back soon!", "See you later!", "Bye, have a great day!", "Take care!"],
            r"thank you|thanks\b": ["You're welcome!", "No problem!", "Happy to help!"]
        }
        # default response when no patterns match
        self.default_response = "Hmm, I'm not sure I understand. Could you rephrase that?"
    def get_response(self, user_input):
        # convert input to lowercase for case insensitive matching
        user_input = user_input.lower().strip()

        # check each regex pattern in the rules
        for pattern, responses in self.rules.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        return self.default_response

    def chat(self):
        # welcome message
        print("Bot: Hi! I'm J.A.R.V.I.S, your rule-based chatbot. Type 'exit' to end our chat.")

        # main conversation loop
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower().strip() in ["exit", "quit", "bye", "goodbye"]:
                    print("Bot: Goodbye! Thanks for chatting!")
                    break
                response = self.get_response(user_input)
                print(f"Bot: {response}")
            except KeyboardInterrupt:
                print("\nBot: Caught you trying to sneak away! Goodbye!")
                break
            except Exception as e:
                print(f"Bot: Oops, something went wrong! Let's try again. (Error: {e})")

# start the chatbot
if __name__ == "__main__":
    chatbot = RuleBot()
    chatbot.chat()