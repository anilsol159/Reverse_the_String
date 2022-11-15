sentence = input("Enter the sentence: ")
words = sentence.split()
reverse_words = []
for word in words:
    reverse = word[::-1]
    print(reverse)
    reverse_words.append(reverse)
    
print(reverse_words)


reversed_sentence = ""
for word in reverse_words:
    if word == reverse_words[-1]:
        reversed_sentence += word
    else:
        reversed_sentence += word+" "
print(reversed_sentence)