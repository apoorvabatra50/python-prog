def permutation(list,comb):
    if (comb==1):
        return list
    else:
        return [a + b
                for a in permutation(list,1)
                for b in permutation(list,comb-1)]

list=["a","b","c"]
print(permutation(list,3))
print(permutation(list,2))
print(permutation(list,1))