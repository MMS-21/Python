import re

def check_password_strength(password):
    """Evaluate the strength of a password and return a rating."""
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password)
    lower_criteria = re.search(r"[a-z]", password)
    digit_criteria = re.search(r"\d", password)
    special_criteria = re.search(r"[@$!%*?&]", password)

    score = sum([length_criteria, bool(upper_criteria), bool(lower_criteria), bool(digit_criteria), bool(special_criteria)])

    if score == 5:
        return "Strong 💪"
    elif 3 <= score < 5:
        return "Moderate ⚙️"
    else:
        return "Weak ⚠️"

if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    user_pass = input("Enter your password: ")
    print("Strength:", check_password_strength(user_pass))
# Example usage:
# print(check_password_strength("P@ssw0rd"))  # Output: Strong