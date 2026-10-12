def bot():
    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot:- Hi!")

        elif user == "how are you":
            print("Bot:- I'm fine, Thanks!")

        elif user == "bye":
            print("Bot:- Goodbye!")
            break

        else:
            print("Bot:- Sorry, I don't understand.")

bot()