def calculator():
    while True:
        try:
            width = float(input("Enter the width of the shape: "))
            if width <= 0:
                print("Width must be greater than 0.")
                continue  # Ask again for valid inputs

            height = float(input("Enter the height of the shape: "))
            if height <= 0:
                print("Height must be bigger than 0:")
                continue

            area = width*height
            perimeter = 2*(width + height)
            print(f"The area of your rectangular shape is {area}")
            print(f"The perimeter of your rectangular shape is {perimeter}")

            user_choice = input("Do you have another calculation in mind?").lower()
            if user_choice != "yes":
                
                print("Exiting, Goodbye!")
                break # Exit loop after successful calculation

        except ValueError:
            print("Invalid input! Please enter numeric values.")
calculator()
 



