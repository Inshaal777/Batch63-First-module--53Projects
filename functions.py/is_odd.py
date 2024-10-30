def main():
    numbers = range(10, 20)

    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

if __name__ == '__main__':
    main()
