
# CyberSafe Toolkit
# A Beginner-Friendly Cybersecurity Project

def password_checker():
    print("\n--- PASSWORD SECURITY ANALYZER ---")

    password = input("Enter your password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("\nPassword Strength:", strength)
    print("Security Score:", score, "/ 5")

    if score < 5:
        print("Suggestion: Use a longer password with")
        print("uppercase, lowercase, numbers and symbols.")
    else:
        print("Good! Your password meets all five checks.")

    print("Note: This is a basic educational checker.")


def url_checker():
    print("\n--- SUSPICIOUS URL CHECKER ---")

    url = input("Enter a URL to examine: ").strip().lower()

    if not url:
        print("Please enter a URL.")
        return

    warnings = []

    if not url.startswith("https://"):
        warnings.append("The URL does not use HTTPS.")

    if "@" in url:
        warnings.append("The URL contains an @ symbol.")

    if "login" in url or "verify" in url or "account" in url:
        warnings.append("The URL contains sensitive-action keywords.")

    if url.count("-") >= 3:
        warnings.append("The URL contains several hyphens.")

    if warnings:
        print("\nPotential warning signs found:")
        for warning in warnings:
            print("-", warning)
    else:
        print("\nNo basic warning signs were detected.")

    print("Important: This is only a basic URL check.")
    print("It cannot confirm whether a website is safe or malicious.")


def security_tips():
    print("\n--- CYBERSECURITY AWARENESS GUIDE ---")

    tips = [
        "Use unique passwords for different accounts.",
        "Enable two-factor authentication.",
        "Never share OTPs or passwords.",
        "Avoid clicking suspicious email links.",
        "Keep your software and devices updated.",
        "Check website addresses before entering details.",
        "Avoid downloading files from unknown sources."
    ]

    for number, tip in enumerate(tips, start=1):
        print(str(number) + ".", tip)


def main():
    while True:
        print("\n================================")
        print("       CYBERSAFE TOOLKIT")
        print("================================")
        print("1. Password Security Analyzer")
        print("2. Suspicious URL Checker")
        print("3. Cybersecurity Awareness Guide")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            password_checker()

        elif choice == "2":
            url_checker()

        elif choice == "3":
            security_tips()

        elif choice == "4":
            print("\nThank you for using CyberSafe!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
