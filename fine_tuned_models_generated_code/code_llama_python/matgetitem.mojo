fn matrix_getitem(self: object, i: object) -> object:
    return self.data[i]


@overload
fn __getitem__(self: object, i: Int) -> object:
    return self.data[i]