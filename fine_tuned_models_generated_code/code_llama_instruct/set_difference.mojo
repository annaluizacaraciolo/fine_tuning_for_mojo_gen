fn difference[T](a: Set[T], b: Set[T]) -> Set[T]:
    # Create a new set.
    var result = Set[T]()

    # Iterate over the elements of the first set.
    for e in a:
        # If the element is not in the second set, add it to the result.
        if e not in b:
            result.add(e)

    # Return the result.
    return result ^[/[

    return difference(b, a)