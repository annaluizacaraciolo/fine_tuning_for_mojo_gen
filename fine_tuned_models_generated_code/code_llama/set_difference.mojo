fn difference(self, other: Self) -> Self:
    # The next link was not correctly generated. The reference expected var result = Set[T]()
    var result = self.copy()
    for e in other:
        if e[] not in other:
            result.add(e[])
    return result^
