def units_enrolled(units):
    print("You have completed " + str(units) + " units.")
    if units >= 60:
        print("Congratulations! You have reached Junior status.")
    else:
        print("Keep going! You'll reach Junior status soon.")

def main():
    unitsCompleted = int(input("Enter the number of units you have completed: "))
    units_enrolled(unitsCompleted)

# Start the program
main()
