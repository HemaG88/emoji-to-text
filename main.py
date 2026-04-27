import emoji

text = input("Enter text with emojis: ")

converted = emoji.demojize(text)

# Remove colons and format nicely
cleaned = converted.replace(":", " ").replace("_", " ")

print("Converted Text:", cleaned)
