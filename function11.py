def convert():
    grams = int(input())
    if grams==0:
        return 0
    return 28.3495231 * grams
ounces = convert()
print(ounces)