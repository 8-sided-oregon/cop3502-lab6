# Main author: Erick Leaf

MENU_STRING = """Menu
-------------
1. Encode
2. Decode
3. Quit
"""

def encode(password):
    return "".join(map(lambda c: str((int(c) + 3) % 10), password))
# Byron Boatright Added Decoder
def decode(encoded_password):
    return "".join(map(lambda c: str((int(c) - 3) % 10), encoded_password))
    
def main():
    encoded = None

    while True:
        print(MENU_STRING)

        selected_option = int(input("Please enter an option: ").strip().split(" ")[0])
        
        if selected_option == 1:
            # User wants to encode a password
            user_input = input("Please enter your password to encode: ")
            # Repeatedly bugs the user until they enter a correct password
            while len(user_input) != 8 or not user_input.isdigit():
                print("Please input a valid 8 digit numeric password!")
                user_input = input("Please enter your password to encode: ")
            encoded = encode(user_input)
            print("Your password has been encoded and stored!")
        elif selected_option == 2:
            # User wants to decode their previously entered password
            if encoded is not None:
                decoded = decode(encoded)
                print(f"The encoded password is: {encoded}, and the original password is: {decoded}.")
        elif selected_option == 3:
            return
        else:
            print("Please input a valid selection (1-3)")

if __name__ == "__main__":
    main()
