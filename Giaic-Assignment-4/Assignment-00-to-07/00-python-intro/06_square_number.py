def main():
    number = float(input("Enter a number: "))
    square = number * number

    print(f"\033[1;3m The square of {number} is {square}.\033[0m")
   
if __name__ == "__main__":
    main()