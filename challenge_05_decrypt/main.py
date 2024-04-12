import string
message = input("Enter the message: ")
shift_num = int(input("Enter the shift number: "))
def decrypt(x,y):
    decrypted_message = ""
    for letter in x:
        if letter in string.ascii_letters:
            new_position = string.ascii_letters.index(letter)
            original_position = (new_position - y) % 52
            decrypted_message += string.ascii_letters[original_position]
        else:
            decrypted_message += letter
    print(f"The encrypted message is:\n*****\n\n{decrypted_message}\n\n*****")
decrypt(x = message, y = shift_num)