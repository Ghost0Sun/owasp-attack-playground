def run_sql_injection():
    print("\n💥 Simulating SQL Injection...\n")

    # Fake users in a pretend database
    fake_users = {"admin": "admin123", "user": "pass"}

    # Simulate user input
    username_input = input("Username: ")
    password_input = input("Password: ")

    # Insecure query simulation (do NOT use in real code!)
    query = f"SELECT * FROM users WHERE username = '{username_input}' AND password = '{password_input}'"
    print(f"\n📄 SQL Query: {query}")

    # Check if it’s a classic SQLi bypass
    if "' OR '1'='1" in username_input or "' OR '1'='1" in password_input:
        print("\n🚨 Injection successful! Logged in without correct credentials.")
    elif username_input in fake_users and fake_users[username_input] == password_input:
        print("\n✅ Login successful (legit credentials).")
    else:
        print("\n❌ Login failed.")

    print("\n💡 Fix: Use parameterized queries or ORM to prevent SQL Injection.")
 
