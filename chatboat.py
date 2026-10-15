def chatbot():
    print("Chatbot: Hello! I am your chatbot.")

    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("Chatbot: Hi!")

        elif message == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif message == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot() 