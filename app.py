# app.py
# Main entrypoint for the Password Strength Checker project.
# Author: Rayan Gorji
# Year: 2026

from getpass import getpass
from password_strength import calculate_score, generate_password

# ========= CONFIG: YOUR LINKS =========
APP_TITLE = "Password Strength Checker"
AUTHOR = "Rayan Gorji"

GITHUB_URL = "https://github.com/RAYANGORJI"
INSTAGRAM_URL = "https://www.instagram.com/rayann_gorji/"
X_URL = "https://x.com/GorjiRayan34159"
LINKEDIN_URL = "https://www.linkedin.com/in/rayan-gr-47663734a/"
FACEBOOK_URL = "https://www.facebook.com/profile.php?id=61579883432824"

# إذا عندك بورتفوليو حقيقي، استبدل هذا اللينك
PORTFOLIO_URL = "Coming soon"


# ========= SIMPLE ANSI COLORS =========
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"


def color(text: str, code: str) -> str:
    return f"{code}{text}{RESET}"


def print_banner() -> None:
    line = "=" * 60
    print(color(line, CYAN))
    print(color(APP_TITLE.center(60), BOLD + CYAN))
    print(color("-" * 60, CYAN))
    print(f"{color('Author   :', BOLD)} {AUTHOR}")
    print(f"{color('GitHub   :', BOLD)} {GITHUB_URL}")
    print(f"{color('Portfolio:', BOLD)} {PORTFOLIO_URL}")
    print(f"{color('Instagram:', BOLD)} {INSTAGRAM_URL}")
    print(f"{color('X:', BOLD)}         {X_URL}")
    print(f"{color('LinkedIn :', BOLD)} {LINKEDIN_URL}")
    print(f"{color('Facebook :', BOLD)} {FACEBOOK_URL}")
    print(color(line, CYAN))


def pause() -> None:
    input(color("\nPress Enter to return to the main menu...", DIM))


def main_menu() -> None:
    while True:
        print_banner()
        print(color("Main Menu:", BOLD + YELLOW))
        print(color("1) Check password strength", GREEN))
        print(color("2) Generate a secure password", GREEN))
        print(color("3) About / Credits", GREEN))
        print(color("4) Exit", RED))

        choice = input(color("Choose an option (1-4): ", BLUE)).strip()

        if choice == "1":
            handle_check_password()
        elif choice == "2":
            handle_generate_password()
        elif choice == "3":
            handle_about()
        elif choice == "4":
            print(color("Goodbye! 👋", MAGENTA))
            break
        else:
            print(color("Invalid option. Please choose 1, 2, 3, or 4.\n", RED))


def handle_check_password() -> None:
    print(color("\n=== Check Password Strength ===", YELLOW))

    username = input("Enter username (optional, press Enter to skip): ").strip() or None
    password = getpass("Enter password to evaluate: ")

    result = calculate_score(password, username=username)

    print(color("\n--- Result ---", CYAN))
    print(f"Score : {result['score']} / 100")
    print(f"Label : {result['label']}")

    print(color("\nFeedback:", MAGENTA))
    if result["feedback"]:
        for line in result["feedback"]:
            print(f"- {line}")
    else:
        print("- No specific feedback. Looks good!")
    print()
    pause()


def handle_generate_password() -> None:
    print(color("\n=== Generate Secure Password ===", YELLOW))

    length_raw = input("Desired length (default 16): ").strip()
    try:
        length = int(length_raw) if length_raw else 16
        if length <= 0:
            raise ValueError
    except ValueError:
        print(color("Invalid length. Using default: 16.", RED))
        length = 16

    print("Include character sets (Y/n):")
    use_lowercase = (input(" - Lowercase letters [a-z]? (Y/n): ").strip().lower() != "n")
    use_uppercase = (input(" - Uppercase letters [A-Z]? (Y/n): ").strip().lower() != "n")
    use_digits = (input(" - Digits [0-9]? (Y/n): ").strip().lower() != "n")
    use_symbols = (input(" - Symbols [!@#$%...]? (Y/n): ").strip().lower() != "n")

    try:
        pwd = generate_password(
            length=length,
            use_lowercase=use_lowercase,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_symbols=use_symbols,
        )
    except ValueError as e:
        print(color(f"Error: {e}", RED))
        print("Returning to main menu.\n")
        pause()
        return

    print(color("\nGenerated password:", GREEN))
    print(color(pwd, BOLD))

    # Optional: evaluate the generated password
    result = calculate_score(pwd)
    print(color("\nEstimated strength:", CYAN))
    print(f"Score : {result['score']} / 100")
    print(f"Label : {result['label']}")
    print()
    pause()


def handle_about() -> None:
    print(color("\n=== About / Credits ===", YELLOW))
    print(color(APP_TITLE, BOLD))
    print(f"Author : {AUTHOR}")
    print(f"GitHub : {GITHUB_URL}")
    print(f"Portfolio: {PORTFOLIO_URL}")
    print(f"Instagram: {INSTAGRAM_URL}")
    print(f"X (Twitter): {X_URL}")
    print(f"LinkedIn : {LINKEDIN_URL}")
    print(f"Facebook : {FACEBOOK_URL}")
    print(
        "\nThis project is created for educational purposes, "
        "to help users understand what makes a strong password."
    )
    print(
        "No passwords are stored or sent anywhere – everything stays in your terminal session."
    )
    print(
        color(
            "\nCopyright (c) 2026 "
            f"{AUTHOR}. All rights reserved.",
            MAGENTA,
        )
    )
    print()
    pause()


if __name__ == "__main__":
    main_menu()