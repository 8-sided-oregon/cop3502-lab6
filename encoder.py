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
            encoded = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif selected_option == 2:
            if encoded is not None:
                decoded = decode(encoded)
                print(f"The encoded password is: {encoded}, and the original password is: {decoded}.")
        elif selected_option == 3:
            return

if __name__ == "__main__":
    main()
