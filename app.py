from calculator import Calculator
from utils import greet

def main():
    calc = Calculator()

    print(greet("Lakshya"))
    print(calc.add(10, 20))
    print(calc.subtract(50, 15))


if __name__ == "__main__":
    main()
