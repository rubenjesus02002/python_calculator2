#src/main.py
from src.introduction import introduction
from src.findaverage import findaverage
from src.comparetoavg import compareToAvg

def main():
    """
    Repeats input loop ten times and prints avgerage and comparisions
    """

    introduction()
    num_sets = 0

    while num_sets < 10:
        num1 = int(input('Enter the first integer: '))
        num2 = int(input('Enter the second integer: '))
        num3 = int(input('Enter the third integer: '))

        print()
        print("the three original integers are:", num1, num2, num3)
        avg = findaverage(num1, num2, num3)
        print(f"The average is {avg:.3f}")

        comparetoavg(num1, num2, num3, avg)
        print()
        num_sets = num_sets + 1

    print(f"Total sets processed: {num_sets}")


