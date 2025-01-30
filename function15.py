from itertools import permutations
def permutation():
    word = str(input())
    new=list(permutations(word))
    print(new)
result = permutation()
