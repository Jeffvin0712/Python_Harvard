# implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 
# and any :( converted to 🙁. All other text should be returned unchanged.

def main():
    text = input("")
    print(convert(text))


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()