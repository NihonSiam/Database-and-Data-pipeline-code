from counter import Counter

print("Program starting...")
print("Initializing counter...")

c = Counter()

print("Counter initialized.")

while True:
    print("\nOptions:")
    print("1) Add count")
    print("2) Get count")
    print("3) Zero count")
    print("4) Exit program")

    choice = input("Choice: ")

    if choice == "1":
        c.addCount()
        print("Count increased")

    elif choice == "2":
        print("Current count:", c.getCount())

    elif choice == "3":
        c.zeroCount()
        print("Count zeroed")

    elif choice == "4":
        print("\nProgram ending.")
        break

    else:
        print("Invalid. Please enter 1, 2, 3, or 4.")
