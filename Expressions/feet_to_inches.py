Inches_in_foot: int = 12

def main():
    feet: float = float(input("Enter number of feet: "))
    inches: float = feet * Inches_in_foot
    print("That is", inches, "inches!")

if __name__ == '__main__':
    main()