
# Basic Rule-Based Chatbot

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Welcome to my chatbot."

    elif user_input == "how are you":
        return "I am fine. Thank you!"

    elif user_input == "what is your name":
        return "I am a Basic Python Chatbot."

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand."


# Main Program

print("Welcome to Basic Chatbot!")
print("You can type hello, how are you, or bye.")

while True:

    user = input("You: ")

    response = chatbot_response(user)

    print("Bot:", response)

    if user.lower().strip() == "bye":
        break
