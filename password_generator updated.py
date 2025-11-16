# Import necessary modules
import string
import secrets
import math

# Blacklist of common weak passwords
BLACKLIST = ["password", "123456", "qwerty", "abc123", "password123", "111111", "welcome", "letmein", "secret" ]


def calculate_entropy(password: str, charset_size: int) -> float:
    """
    Calculate entropy in bits for a given password.
    Entropy = log2(charset_size^length)
    """
    length = len(password)
    entropy = length * math.log2(charset_size)
    return entropy

def password_strength(entropy: float) -> str:
    """
    Classify password strength based on entropy.
    """
    if entropy < 28:
        return "Weak"
    elif entropy < 36:
        return "Moderate"
    elif entropy < 60:
        return "Strong"
    else:
        return "Very Strong"

# Define Blacklist
def is_blacklisted(password: str) -> bool:
    return password.lower() in BLACKLIST

# Define the password generator function
def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    # Start with lowercase letters
    characters = string.ascii_lowercase
    
    # Add character types based on user preferences
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    # Randomly select characters to build the password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    # Check blacklist
    if is_blacklisted(password):
        print("Generated a weak/common password, regenerating...")
        return generate_password(length, use_upper, use_digits, use_symbols)
    
    # Calculate entropy
    entropy = calculate_entropy(password, len(characters))
    strength = password_strength(entropy)

    print(f"Generated password: {password}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Strength: {strength}")

    return password, entropy, strength


# Validate yes/no inputs
def get_yes_no(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['y','n']:
            return response == 'y'
        else:
            print("Please enter 'y' or 'n'.")


# Main loop
while True:
    # Validate password length
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length < 4:
                 print("Password should be at least 4 characters long.")
            else:
                   break
        except ValueError:
           print("Please enter a valid number.") 
    # Ask the user for password preferences
    use_upper = get_yes_no("Include uppercase letters? (y/n): ")
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")
    #Generate and display the password
    print("Generated password:", generate_password(length, use_upper, use_digits, use_symbols))
    # Ask if they want another one
    again = get_yes_no("Generate another password? (y/n): ")
    if not again:
        print("Goodbye!")
        break
        







   
