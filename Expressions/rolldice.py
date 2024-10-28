import random
Num_sides: int = 6

def main():
    die1: int = random.randint(1, Num_sides)
    die2: int = random.randint(1, Num_sides)
    total: int = die1 + die2

    print("Dice have", Num_sides, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()