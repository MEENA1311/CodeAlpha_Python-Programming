# Simple Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input == "hello":
        return "hi"
    elif user_input == "how are you":
        return "i am fine, thanks!"
    elif user_input == "bye":
        return "goodbye"
    else:
        return "i don't understand."

# Chat loop
print("Chatbot: Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    if user_input.lower() == "bye":
        break
