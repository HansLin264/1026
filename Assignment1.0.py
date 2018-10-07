#Lists for valid inputs
beverage_type_coffee = ["coffee" , "c"]
beverage_type_tea = ["t" , "tea"]
beverage_size_options = ["large" , "medium" , "small" , "s" , "l" , "m"]
beverage_coffee_options = ["none" , "" , "v" , "vanilla" , "c" , "chocolate"]
beverage_tea_options = ["none" , "" , "m" , "l" , "mint", "lemon"]

# These variables were defined here to calculate cost variable later
price_size = 0
price_flavor = 0
cost = 0.0

customer_name = input("Hello, what is your name (No spaces or numbers): ")
if not str.isalpha(customer_name): # Used .isalpha to test input for anything but string, prompts my "invalid" when there is a number or space and prompts exit()
    print("Invalid input, please select a valid option:")
    exit()
else:
    beverage_type = input("Select type of beverage (coffee, or tea): ")
    beverage_type = beverage_type.lower() # Lowercase the input before invalid statement in line 104

    if beverage_type in beverage_type_coffee: # If they chose coffee as beverage type
        beverage_size = input("Select the size of the beverage (large, medium, small): ")
        beverage_size = beverage_size.lower()
        beverage_type = "coffee"

        while not beverage_size in beverage_size_options:
            print("Invalid input, please select a valid option:")
            exit()

        if beverage_size == "large" or beverage_size == "l":
            price_size = 3.25
            beverage_size = "large"
        elif beverage_size == "medium" or beverage_size == "m":
            price_size = 2.50
            beverage_size = "medium"
        elif beverage_size == "small" or beverage_size == "s":
            price_size = 1.50
            beverage_size = "small"

        beverage_flavor = input("Select added flavorings (Press enter or type 'none', vanilla, chocolate): ")
        beverage_flavor = beverage_flavor.lower()

        while not beverage_flavor in beverage_coffee_options:
            print("Invalid input, please select a valid option:")
            exit()

        if beverage_flavor == "none" or beverage_flavor == "":
            beverage_flavor = "no flavoring"
            price_flavor = 0.0
        elif beverage_flavor == "vanilla" or beverage_flavor == "v":
            beverage_flavor = "vanilla flavoring"
            price_flavor = 0.25
        elif beverage_flavor == "chocolate" or beverage_flavor == "c":
            beverage_flavor = "chocolate flavoring"
            price_flavor = 0.75

        cost = float((price_flavor + price_size)*1.13) #caluculated cost then rounded and used in print statement
        final_cost = float(cost)
        final_cost = round(final_cost, 2)
        print("For " + customer_name + ", a " + beverage_size + " " + beverage_type + ", " + beverage_flavor + ", cost: $" + str(final_cost))

    elif beverage_type in beverage_type_tea: # If they chose tea as their beverage type
        beverage_size = input("Select the size of the beverage (large, medium, small): ")
        beverage_size = beverage_size.lower()
        beverage_type = "tea"

        while not beverage_size in beverage_size_options:
            print("Invalid input, please select a valid option:")
            exit()

        if beverage_size == "large" or beverage_size == "l":
            price_size = 3.25
            beverage_size = "large"
        elif beverage_size == "medium" or beverage_size == "m":
            price_size = 2.50
            beverage_size = "medium"
        elif beverage_size == "small" or beverage_size == "s":
            price_size = 1.50
            beverage_size = "small"

        beverage_flavor = input("Select added flavorings (Press enter or type 'none', lemon, mint): ")
        beverage_flavor = beverage_flavor.lower()

        while not beverage_flavor in beverage_tea_options:
            print("Invalid input, please select a valid option:")
            exit()

        if beverage_flavor == "none" or beverage_flavor == "":
            price_flavor = 0.0
            beverage_flavor = "no flavoring"
        elif beverage_flavor == "lemon" or beverage_flavor == "l":
            price_flavor = 0.25
            beverage_flavor = "lemon flavoring"
        elif beverage_flavor == "mint" or beverage_flavor == "m":
            price_flavor = 0.50
            beverage_flavor = "mint flavoring"

        cost = float((price_flavor + price_size)*1.13)
        final_cost = float(cost)
        final_cost = round(final_cost, 2)
        print("For " + customer_name + ", a " + beverage_size + " " + beverage_type + ", " + beverage_flavor + ", cost: $" + str(final_cost))

    else:
        print("Invalid input, please select a valid option:") # "invalid" for beverage type
        exit()




