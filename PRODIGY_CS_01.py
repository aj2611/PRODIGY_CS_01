def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Preserve case
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ('e', 'd'):
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter the shift value (e.g. 3): "))
    except ValueError:
        print("Invalid shift. Must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted)

if _name_ == "_main_":
    main()