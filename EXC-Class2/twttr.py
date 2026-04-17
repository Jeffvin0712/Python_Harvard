vocals = "aeiou"
results = ""
text = input("Input: ")

for l in text:
    if l.lower() not in vocals:
        results += l

print(f"Output: {results}", end="")
