def reverse(n):
    return n[::-1]

def ispalendrom(str):
    if str== reverse(str):
        return True
    else:
        return False


strin= ispalendrom(input("input your string here"))

if strin==True:
    print("string is palendrom")
else:
    print("not a palendrom")