while True:
    try:
        num = int(input("Enter a number (0 to exit): "))
        if num == 0:
            print("Exiting...")
            break
        elif num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Please enter a valid integer.")
