# hello_friend.py
# A very simple program for beginners (Hacktoberfest idea)

def greet(name):
    return f"Hello, {name}! 👋 Hope you're having a great day!"

def main():
    print("Welcome to Hello Friend! 😊")
    name = input("What's your name? ")
    print(greet(name))

if __name__ == "__main__":
    main()
