## This program converts kilometers to miles.

def main():
    keep_going = "Y"
    print("The conversion between kilometers and miles is:" +
          "\n\tMiles = Kilometers x 0.6214")
    print()
    while keep_going.upper() == "Y":
        distance = float(input("Enter the distance in kilometers: "))
        convert_distance(distance)
        keep_going = input("Would you like to do another conversion?" +
                        "(Y for yes, N for no): ")
        print()

    input("Press the Enter key to terminate the program...")



def convert_distance(km):
    miles = km * 0.6214
    print("That converts to:",format(miles, ',.2f'))
    

main()
