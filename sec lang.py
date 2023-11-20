import random

print("Enter whether you want to code or decode:\n")
x = input()

if x == "code":
    a = input("Enter the content to make it secretly framed:\n ")
    words = a.split()
    secret_words = []
    for word in words:
        word_list = list(word)
        word_list.append(word_list[0])
        word_list.remove(word_list[0])
        z = ["strd", "rhrb", "egnf", "iuyi", "lopk", "jvdn"]
        word_list.insert(2, random.choice(z))
        secret_words.append(''.join(word_list))
    secret_sentence = ' '.join(secret_words)
    print(secret_sentence)
elif x == "decode":
    b = input("Enter the content to decode:\n ")
    words = b.split()
    decoded_words = []
    for word in words:
        word_list = list(word)
        e = word_list.copy()
        d = e[-1]
        word_list.insert(0, d)
        word_list.remove(word_list[3])
        word_list.remove(word_list[3])
        word_list.remove(word_list[3])
        word_list.remove(word_list[3])
        word_list = word_list[:len(word_list)-1]

        decoded_words.append(''.join(word_list))
    decoded_sentence = ' '.join(decoded_words)
    print(decoded_sentence)
else:
    print("INVALID")        