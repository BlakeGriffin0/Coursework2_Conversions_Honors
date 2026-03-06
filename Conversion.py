# ------------------------------------------------------------
# PROG 1003H – Spring 2026
# HW-3H – Conversions
# Solution by Blake Griffin
# ------------------------------------------------------------


# ------------------------------------------------------------
# Conversion Dictionaries
# Base Units:
# Length  -> meters
# Volume  -> liters
# Weight  -> grams
# ------------------------------------------------------------

length_units = {
    1: ("Inches", 0.0254),
    2: ("Feet", 0.3048),
    3: ("Meters", 1.0),
    4: ("Kilometers", 1000.0),
    5: ("Hands", 0.1016),
    6: ("Furlongs", 201.168),
    7: ("Rods", 5.0292)
}

volume_units = {
    1: ("US Ounces", 0.0295735),
    2: ("US Gallons", 3.78541),
    3: ("Liters", 1.0),
    4: ("US Fluid Barrels", 119.240935),
    5: ("US Teaspoons", 0.00492892),
    6: ("Cubic Feet", 28.3168),
    7: ("Tuns", 953.923769)
}

weight_units = {
    1: ("Pounds", 453.59237),
    2: ("Grams", 1.0),
    3: ("Dram", 1.7718451953125),
    4: ("Grain", 0.06479891),
    5: ("Ounce", 28.349523125),
    6: ("Stone", 6350.29318),
    7: ("Talent", 34000.0)
}


# ------------------------------------------------------------
# Functions to get number, display menus, and perform conversions.
# ------------------------------------------------------------

def print_header():
    print("HW-3H – Conversions")
    print("Solution by YOUR FIRST AND LAST NAME")
    print()


def get_valid_number():
    while True:
        try:
            value = float(input("Enter a positive number (less than 1000): "))
            if 0 < value < 1000:
                return value
            else:
                print("Value must be greater than 0 and less than 1000.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def display_main_menu():
    print("\nSelect a Category:")
    print("1. Length")
    print("2. Volume")
    print("3. Weight")


def get_category_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice in (1, 2, 3):
                return choice
            else:
                print("Invalid selection. Choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid integer.")


def display_unit_menu(units_dict, category_name):
    print(f"\nSelect a {category_name} Unit:")
    for key in units_dict:
        print(f"{key}. {units_dict[key][0]}")


def get_unit_choice(units_dict):
    while True:
        try:
            choice = int(input("Enter your unit choice (1-7): "))
            if choice in units_dict:
                return choice
            else:
                print("Invalid unit selection. Choose 1-7.")
        except ValueError:
            print("Please enter a valid integer.")


def convert_to_base(value, factor):
    return value * factor


def convert_from_base(base_value, factor):
    return base_value / factor


def display_results(value, unit_choice, units_dict):
    unit_name, factor = units_dict[unit_choice]

    print("\nOriginal Value:")
    print(f"{value:,.4f} {unit_name}")
    print("-" * 40)
    print("Converted Values:")

    base_value = convert_to_base(value, factor)

    for key in units_dict:
        if key != unit_choice:
            name, unit_factor = units_dict[key]
            converted = convert_from_base(base_value, unit_factor)
            print(f"{converted:,.4f} {name}")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print_header()

while True:

    value = get_valid_number()

    display_main_menu()
    category_choice = get_category_choice()

    if category_choice == 1:
        units_dict = length_units
        category_name = "Length"
    elif category_choice == 2:
        units_dict = volume_units
        category_name = "Volume"
    else:
        units_dict = weight_units
        category_name = "Weight"

    display_unit_menu(units_dict, category_name)
    unit_choice = get_unit_choice(units_dict)

    display_results(value, unit_choice, units_dict)

    again = input("\nDo you want to perform another conversion? (y/n): ").lower()
    if again != 'y':
        break

print("\nHW-3H Complete")