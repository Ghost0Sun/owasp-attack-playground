import re

def run_weak_auth():
    print("\n🔓 Simulating Weak Authentication...\n")

    password = input("Set a new password: ")

    # Weak password check
    if len(password) < 6:
        print("❌ Weak: Too short (less than 6 characters)")
    elif password.isdigit():
        print("❌ Weak: Numbers only")
    elif password.lower() in ["password", "123456", "qwerty"]:
        print("❌ Weak: Common dictionary password")
    elif not re.search(r"[A-Z]", password):
        print("❌ Weak: No uppercase letters")
    else:
        print("✅ Looks strong enough!")

    print("\n💡 Fix: Enforce password policies, use hashing (bcrypt), and avoid common passwords.")
