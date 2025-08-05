# src/main.py
from src.introduction import introduction
from src.findaverage import findaverage
from src.comparetoavg import compareToAvg

def main():
    """
    Repeats input loop 10 times and prints average and comparisons.
    """
    introduction()
    num_sets = 0

    while num_sets < 10:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))

        avg = findaverage(num1, num2, num3)
        print(f"The average is {avg:.3f}")
        print()

        compareToAvg(num1, num2, num3, avg)
        print()
        num_sets += 1

    print(f"Total sets processed: {num_sets}")

if __name__ == "__main__":
    main()