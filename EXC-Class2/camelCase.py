def camelCase():
    text = input("camelCase: ")
    print(f"snake_case: {convert(text)}")

def convert(c):
    result = ""
    for l in c:
        if l.isupper():
            result += "_" + l.lower()
        else:
            result += l
    return result

camelCase()