from sql_injection import run_sql_injection
from broken_access import run_broken_access
from weak_auth import run_weak_auth
from utils import clear_screen, print_title

def main():
    while True:
        clear_screen()
        print_title("🛡️ OWASP Attack Playground")

        print("Choose a vulnerability to simulate:\n")
        print("1. SQL Injection in Login")
        print("2. Broken Access Control")
        print("3. Weak Authentication")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_sql_injection()
            input("\nPress Enter to go back to menu...")
        elif choice == "2":
            run_broken_access()
            input("\nPress Enter to go back to menu...")
        elif choice == "3":
            run_weak_auth()
            input("\nPress Enter to go back to menu...")
        elif choice == "4":
            print("\nGoodbye! Stay safe 👋")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

