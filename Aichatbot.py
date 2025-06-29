import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# First-time downloads
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Basic responses (pattern-response pairs)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a Chatbot created using Python."]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?", "All good here!"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry", "It's okay"]
    ],
    [
        r"quit",
        ["Bye! Have a nice day.", "It was nice talking to you!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?", "Interesting... tell me more!"]
    ]
]

# Chatbot class using NLTK
def chatbot():
    print("🤖 Hello! I am a simple AI chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
