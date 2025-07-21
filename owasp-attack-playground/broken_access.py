def run_broken_access():
    print("\n🚨 Simulating Broken Access Control...\n")

    # Simulating two users: user and admin
    users = {
        "user": {"role": "user", "files": ["profile.txt"]},
        "admin": {"role": "admin", "files": ["profile.txt", "secret_admin_file.txt"]}
    }

    # Simulate login
    username = input("Enter your username (user/admin): ").strip().lower()

    if username not in users:
        print("❌ Unknown user.")
        return

    print(f"\n✅ Logged in as {username} (role: {users[username]['role']})")

    # Let user try to access a specific file
    file_to_access = input("Which file do you want to access? ")

    # Check access
    if file_to_access in users[username]["files"]:
        print(f"\n📂 Access granted to '{file_to_access}'")
    else:
        print(f"\n🚨 Access Denied! You are not authorized to access '{file_to_access}'")

        # Simulate insecure direct object reference
        print("\n[!] However... due to insecure file checks, the system still serves it:")
        print(f"\n📄 Contents of '{file_to_access}': [REDACTED DATA DUMP]")

    print("\n💡 Fix: Always check user roles before serving sensitive resources.")
