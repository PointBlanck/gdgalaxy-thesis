""" Main module of thesis. """

# Import necessary modules
import precalculation as pc

def main():
    """ Main function """

    # Welcome message
    print(100*"=")
    print("Numeric calculation of spiral-maintaining family of orbits in Grand Design galaxies")
    print(100*"=")

    # Ask user for input
    precalc = input("Q1: Would you like to inspect the model via plots?")
    if precalc.lower() == "y":
        max_r = input("Input: max_r\n")
        max_r = int(max_r)
        text = input("Input: dim(r), dim(phi)\n")
        N_r, N_phi = text.split(",")
        N_r = int(N_r.strip())
        N_phi = int(N_phi.strip())
        print("Plotting potentials...")
        pc.plot_potentials(max_r, N_r, N_phi)
    elif precalc.lower() == "n":
        print("\nPrecalculation denied.")
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