""" Main module of thesis. """

# Import necessary modules
import precalculation as pc
import integration as ints

def main():
    """ Main function """

    # Welcome message
    print(100*"=")
    print("Numeric calculation of spiral-maintaining family of orbits in Grand Design galaxies")
    print(100*"=")

    # Ask user for input
    precalc = input("Q1: Would you like to inspect the model via plots? (y/n)")
    if precalc.lower() == "y":
        pc.plots()
    elif precalc.lower() == "n":
        print("\nPrecalculation denied.")
    else:
        return 1
    
    # Integrate system.
    ints.integrate()
    print("Main terminated successfully")
    return 0


if __name__ == "__main__":
    info = main()
    if info == 0:
        print("Program terminated successfully")
    else:
        print("\nXXX: Something went wrong.")