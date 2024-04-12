import string
message = input("Enter a message: ")
shift_num = int(input("Enter a shift number: "))
def encrypt(x,y):
    encrypted_message = ""
    for letter in x:
        if letter in string.ascii_letters:
            original_position = string.ascii_letters.index(letter)
            new_position = (original_position + y) % 52
            encrypted_message += string.ascii_letters[new_position]
        else:
            encrypted_message += letter
    print(f"The encrypted message is:\n{encrypted_message}")
encrypt(x = message, y = shift_num)