# Implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

# ///////////////////////////////////////////
# text = input("")
# print(text.replace(" ", "..."))
# ///////////////////////////////////////////

while True:
    try:
        user_input = input("Enter something: ")
        print(user_input.replace(" ", "..."))
    except (EOFError, KeyboardInterrupt):
        print("Thanks, GoodBye")
        break