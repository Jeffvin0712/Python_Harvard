# Implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
# Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, 
# as by passing a str of your own as an argument to input.

# ///////////////////////////////////////////
# text = input("").lower()
# print(text)
# ///////////////////////////////////////////

while True:
    try:
        user_input = input("Enter something: ")
        print(user_input.lower())
    except (EOFError, KeyboardInterrupt):
        print("Thanks, GoodBye")
        break
    