import random
Num_sides = 6

def roll_dice():
    die1: int = random.randint(1, Num_sides)
    die2: int = random.randint(1, Num_sides)
    print(die1)
    print(die2)
    total : int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()