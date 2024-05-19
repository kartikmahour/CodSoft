def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for easier matching
    
    # Define predefined rules and responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main function to interact with the chatbot
def main():
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print(chatbot_response(user_input))
            break
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
