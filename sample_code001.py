def greet(name):
    return f"Hello, {name}!"

def calculate_sum(a, b):
    return a + b

def main():
    print("Hello, World!")
    print("This is a sample Python script create in develop branch .")
    
    name = "Python"
    greeting = greet(name)
    print(greeting)
    
    num1 = 10
    num2 = 20
    result = calculate_sum(num1, num2)
    print(f"Sum of {num1} and {num2} is: {result}")
    
    numbers = [1, 2, 3, 4, 5]
    print(f"Numbers: {numbers}")
    print(f"Sum of numbers: {sum(numbers)}")

if __name__ == "__main__":
    main()