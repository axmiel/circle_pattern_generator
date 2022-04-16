from turtle import *
go_again = True
valid = ["Y", "N"]
redo = 'X'
while go_again:
    try:
        get_number = int(input("How many circles?: "))
    except ValueError:
        print("Please only use positive whole numbers")
    else:
        if get_number < 1:
            print("Please only use positive whole numbers")
        else:
            if get_number > 10:
                print("This might take a while...")
            for circle in range(get_number):
                for i in range(45):
                    forward(8)
                    left(8)
                left(360/get_number)
            redo = 'X'
            while redo.capitalize() not in valid:
                redo = input("Go again? (Y/N): ")
                if redo.capitalize() not in valid:
                    print("Your answer must be either Y or N")
                elif redo.capitalize() == valid[0]:
                    clear()
                    go_again = True
                else:
                    go_again = False
                    print("Thanks for playing!")
