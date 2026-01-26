
INCH_TO_METER = 0.0254

def inches_to_meters(inches):
    return inches * INCH_TO_METER

def main():
    try:
        inches = float(input("Enter the value in inches: "))
        meters = inches_to_meters(inches)
        print(f"{inches} inches is equal to {meters:.4f} meters.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
        main()


def inch_to_cms():
    inches = float(input("Enter the value in inches: "))
    cms = inches * 2.54
    print("Value in cms is:", cms)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(11))

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)




