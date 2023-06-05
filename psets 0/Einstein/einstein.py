# Einstein E=mc^2

def main():
    # Prompt the user for mass input
    mass = int(input("Enter the mass in kilograms: "))
    # Calculate the equivalent energy
    energy = calculate_energy(mass)
    # Output the result
    print('The equivalent energy is', energy, "Joules.")


def calculate_energy(mass):
    speed_of_light = 300000000  # meters per second
    energy = mass * speed_of_light ** 2
    return energy


main()
