fn fibonacci(n: Int) -> Int:
    if n < 2:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)

# Code bellow was added in order to easily test the generated code above
def main():
    print(fibonacci(4))