""" Main module of thesis. """

import precalculation as pc

def main():
    """ Main function """

    # Welcome message
    print(100*"=")
    print("Numeric calculation of spiral-maintaining family of orbits in Grand Design galaxies")
    print(100*"=")

    # Ask use for input
    precalc = input("Q1: Would you like to inspect the model via plots?")
    if precalc.lower() == "y":
        pc.plot_potentials()
    else:
        return 1
    print("Main terminated successfully")
    return 0


if __name__ == "__main__":
    info = main()
    if info == 0:
        print("Program terminated successfully")
    else:
        print("\nXXX: Something went wrong.")