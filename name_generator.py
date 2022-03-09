import sys, random


def name_generator():

    print("Welcome to the D&D Name Generator. \n")
    print("A name for your brand new, on-the-spot NPC:\n")

    firstNames = []
    with open("firstnames.txt", "r") as infile:
        for line in infile:
            line = line.strip(".0123456789 ")
            firstNames.append(line)

    lastNames = []
    with open("lastnames.txt", "r") as infile:
        for line in infile:
            line = line.strip(".0123456789 ")
            lastNames.append(line)

    while True:

        firstName = random.choice(firstNames)
        lastName = random.choice(lastNames)
        print(f"{firstName}{lastName}")

        try_again = input("\nTry again? (Press Enter, else press n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("Press Enter to exit.")


if __name__ == "__main__":
    name_generator()
