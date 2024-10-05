import re

def assess_password_strength(password):
    # Initializing scores and feedback
    score = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 12:
        score += 2
        feedback.append("Good length.")
    elif len(password) >= 8:
        score += 1
        feedback.append("Moderate length, but longer is better.")
    else:
        feedback.append("Too short. Password should be at least 8 characters long.")

    # Criteria 2: Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("No uppercase letters. Add some for more strength.")

    # Criteria 3: Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("No lowercase letters. Add some for more strength.")

    # Criteria 4: Numbers
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("No numbers. Add some for more strength.")

    # Criteria 5: Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("No special characters. Add some for more strength.")

    # Overall feedback on password strength
    if score >= 6:
        overall_feedback = "Strong password."
    elif 4 <= score < 6:
        overall_feedback = "Moderate password."
    else:
        overall_feedback = "Weak password."

    # Output result
    return {
        "password": password,
        "score": score,
        "feedback": feedback,
        "overall_feedback": overall_feedback
    }


# Example usage
password = input("Enter a password to assess its strength: ")
result = assess_password_strength(password)

print("\nPassword Strength Assessment:")
print(f"Password: {result['password']}")
print(f"Score: {result['score']} / 6")
print(f"Overall Feedback: {result['overall_feedback']}")
print("Detailed Feedback:")
for item in result['feedback']:
    print(f"- {item}")
