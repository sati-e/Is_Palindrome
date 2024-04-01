# is this word a palindrome?
print("Is this word a palindrome?")


def is_palindrome(word):
    w = word.lower()
    return w == w[::-1]


input_word = input("Type a word: ")

if input_word.isalpha():
    if is_palindrome(input_word):
        print("This word is a palindrome!")
    else:
        print("This word is not a palindrome...")
else:
    print("Error")
