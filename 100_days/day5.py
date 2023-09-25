#Caeser Cipher
def caeser_cipher(opt,text,shift_amount):
    ans=""
    if opt=="decode":
        shift_amount*=-1
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift_amount
            ans+=alphabet[new_position]
        else:
            ans+=char
    print(f"Here is your {opt}ed text: {ans}")

should_end=False
while not should_end:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    operation=input("Type \"encode\" for encrypt or \"decode\" for decrypt\n")
    message=input("Type your message: ")
    shift_number=int(input("Enter your shift number: "))
    shift_number=shift_number%26

    caeser_cipher(operation,message,shift_number)

    restart=input("Type yes for start again otherwise no: ").lower()
    if restart=="no":
        should_end=True
        print("Bye")