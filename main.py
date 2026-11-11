text = input("Paste some text: ")
chars = len(text)
words = len(text.split())
tokens = round(chars / 4)  # about 4 characters per token in English

print(f"Characters: {chars}")
print(f"Words: {words}")
print(f"Estimated tokens: {tokens}")

pages = int(input("How many pages? "))
print(f"About {pages * 500} words")