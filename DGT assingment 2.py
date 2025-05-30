def calculator():
    while True:
        try:
            length = float(input("Enter the length of the fence: "))
            if length <= 0:
                print("Length must be bigger than 0:")
                continue
            width = float(input("Enter the width of the fence: "))
            if width <= 0:
                print("Width must be greater than 0.")
                continue  # Ask again for valid inputs
            cost_per_metre = float(input("Enter cost per meter: "))
            if cost_per_metre <= 0:
                print("Cost per metre must be greater than 0.")
                continue
            perimeter = 2*(length*width)

            total_cost = perimeter * cost_per_metre
            print(f"The total cost to fence your {perimeter}m rectangular area is {total_cost}")

            user_choice = input("Do you have another calculation in mind? ")
            if user_choice !="":
                print("Exiting, Goodbye!")
                break # Exit loop after successful calculation

        except ValueError:
            print("Invalid input! Please enter numeric values.")
calculator()
