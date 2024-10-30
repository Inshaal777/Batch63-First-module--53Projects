def main():
    num: int = 7
    num = subtract_seven(num)
    print("this should be zero: ", num)

def subtract_seven(num):
    num = num - 5
    return num

if __name__ == '__main__':
    main()