text = 'Define which data represents "ham" class and which data represents "spam" class for the machine-learning algorithm.'
text = "i. e."
delimiters = ['"', "."]
words = []
current_word = ""
for char in text:
    if char==" ":
        if not current_word=="":
            words.append(current_word)
            current_word = ""
    elif char in delimiters:
        if current_word=="":
            words.append(char)
        else:
            words.append(current_word)
            words.append(char)
            current_word = ""
    else:
        current_word += char

print(words)
