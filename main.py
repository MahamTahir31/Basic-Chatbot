import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import random


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

responses = {
    "greeting": ["Hi there!", "Hello!", "How can I help you today?"],
    "question": ["I'm not sure, can you provide more details?"],
    "thanks": ["You're welcome!", "Happy to help."],
    "goodbye": ["Goodbye!", "See you later!"]
}

def process_input(user):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(user.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens

def chatbot_conversation():
    print("\nHi there! I'm your friendly chatbot. How can I help you today?")

    while True:
        user_input = input("> ")
        tokens = process_input(user_input)

        if any(token in tokens for token in ["hi", "hello", "greetings"]):
            print(random.choice(responses["greeting"]))
        elif any(token in tokens for token in ["question", "how", "what", "why"]):
            print(random.choice(responses["question"]))
        elif any(token in tokens for token in ["thanks", "thank you"]):
            print(random.choice(responses["thanks"]))
        elif any(token in tokens for token in ["goodbye", "bye"]):
            print(random.choice(responses["goodbye"]))
            break
        else:
            print("I'm not sure I understand. Can you rephrase your question?")


chatbot_conversation()