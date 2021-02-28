import sys, random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


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


# creates an instance of the application object
app = QApplication(sys.argv)

# creates an instance of the application's gui
window = QWidget()
window.setWindowTitle("D&D Name Generator")
window.setGeometry(100, 100, 500, 80)
window.move(60, 15)
helloMsg = QLabel("<h1>Welcome to the Name Generator</h1>", parent=window)
helloMsg.move(60, 15)

# show the gui
window.show()

# run app event loop (or main loop)
sys.exit(app.exec_())
