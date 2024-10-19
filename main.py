

#encoder by Michael Wei (I am signed into my Mwei1 Github account yet it is attributing it to dipplydopply, my personal one)
#adds 3 to every digit in the password
def encode(password):
    encoded = ""
    for i in password:
        encoded += str((int(i)+3) % 10)
    return encoded

def decode(code):
    decoded_password = ''
    for char in code:  # loops through each character in the encoded password
        decoded_digit = (int(char) - 3) % 10  # shifts characters back by 3
        decoded_password += str(decoded_digit)
    return decoded_password  # return final decoded password

#main function
def main():
    #stored code
    code = None
    while True:
        #print menu
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")
        response = input("Please enter an option: ")

        #encoder
        if response == "1":
            password = input("Please enter your password to encode: ")
            code = encode(password)
            print("Your password has been encoded and stored!\n")

        #decoder
        elif response == "2":
            print(f"The encoded password is {code}, and the original password is {decode(code)}.")

        #exit
        elif response == "3":
            break
        #invalid input
        else:
            print("Invalid option! Please try again.")
            continue





#main method
if __name__ == "__main__":
    main()