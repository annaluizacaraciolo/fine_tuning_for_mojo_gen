if __name__ == '__main__':
    context = """ Mojo is a new programming language developed with focus on machine learning. It is supposed to be a superset of Python and support Python syntax. However, Mojo is—first and foremost—designed for high-performance systems programming, with features like strong type checking, memory safety, next-generation compiler technologies, and more. 
                In Mojo, a parameter is a compile-time variable that becomes a runtime constant, and it's declared in square brackets on a function or struct. Parameters allow for compile-time metaprogramming, which means you can generate or modify code at compile time.
                Code blocks such as functions, conditions, and loops are defined with a colon followed by indented lines. 
                Mojo supports two types of functions: def and fn functions. You can use either declaration with any function, including the main() function, but they have different default behaviors, as described on this page. Functions declared inside a struct are called "methods," but they have all the same qualities as "functions" described here.
                If you don't declare the type for an argument or return value in a def, it becomes an object, which is unlike any other type in the standard library.
                The object type allows for dynamic typing because it can actually represent any type in the Mojo standard library, and the actual type is inferred at runtime. 
                Here's everything to know about def:
                Arguments don't require a declared type.
                Undeclared arguments are actually passed as an object, which allows the function to receive any type (Mojo infers the type at runtime).
                Return types don't need to be declared and also default to object.
                Arguments are mutable (usually passed by value, using the owned argument convention).
                If an argument is an object type, it's received as a reference, following object reference semantics.
                If an argument is any other declared type, it's received as a value (using the owned argument convention).
                Variables don't need to be declared using var.
                Here's everything to know about fn:
                Arguments must specify a type (except for the self argument in struct methods).
                Return values must specify a type, unless the function doesn't return a value.
                If you don't specify a return type, it defaults to None (meaning no return value).
                By default, arguments are received as an immutable reference (values are read-only, using the borrowed argument convention).
                This prevents accidental mutations, and permits the use of non-copyable types as arguments.
                If you want a local copy, you can simply assign the value to a local variable. Or, you can get a mutable reference to the value by declaring the inout argument convention).
                Variables must be declared using the var keyword.
                If the function raises an exception, it must be explicitly declared with the raises keyword. (A def function does not need to declare exceptions
                Mojo supports type alias, tensors, vector, list, set, bool, Float, Int, SIMD and more.
                Mojo provides a benchmark and testing modules.
                Mojo decorator is a higher-order function that modifies or extends the behavior of a struct, a function, or some other code. Instead of actually calling the higher-order function, you simply add the decorator (such as the @value decorator) above your code (such as a struct). The Mojo compiler then uses the decorator function to modify your code at compile time. Example: You can add the @always_inline decorator on any function to make the Mojo compiler inline the body of the function directly into the body of the calling function."""

    prompt =    '''fn difference(self, other: Self) -> Self:
                    if e[] not in other:
                        result.add(e[])
                    return result^
                ''' 

    # Prompts for Instruct
    # "Write a function to calculate the sum of two integers."
    # "Write a function to calculate the nth fibonacci number."
    # "Write a function to calculate the difference between two set structures."

    # Prompts for Infilling
    # '''fn sum(a: Int, b: Int)'''

    # ''' fn fibonacci(
    # return fibonacci(n - 2) + fibonacci(n - 1)
    # '''

    # '''fn difference(self, other: Self) -> Self:
    #       if e[] not in other:
    #           result.add(e[])
    #       return result^
    # '''

    # Prompts for Completion
    # "fn sum(a: Int, b: Int)"
    # 'fn fibonacci('
    # '''fn difference(self, other: Self) -> Self:
	#	    var result = Set[T]()
    #       for e in self:'''

    print(len(context))
    print("total length: {}".format(len(context) + len(prompt)))