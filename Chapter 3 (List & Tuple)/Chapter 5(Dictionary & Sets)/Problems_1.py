Words= {
    "hello": "A greeting",
    "Madad": "Help",
    "Python": "A programming language",
    "Dhruv": "A name",
    "Sher": "Lion",
}

word= (input("Enter the word  you want to meaning of : "))
if word in Words:
    print(Words[word])
else:
    print("Word not found.")