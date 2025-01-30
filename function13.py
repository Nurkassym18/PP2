def solve(numheads, numlegs):
    b = (numlegs/2)-numheads
    a = ((numlegs/2))-2*b
    return f"{int(a)},{int(b)}"
values = solve(20,58)
print(values)
