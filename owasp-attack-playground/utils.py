import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title(title):
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()
 
