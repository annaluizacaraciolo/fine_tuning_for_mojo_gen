# Code generated matched the reference exactly
fn difference(self, other: Self) -> Self:
    var result = Set[T]()
    for e in self:
        if not e in other:
            result.add(e[])
    return result ^
