# nth prime no.
class CCalculate:
    def __init__(self):
        pass

    def IsEven(self, num):
        if num % 2 == 0:
            return True
        return False


# Derived class
class CPrime(CCalculate):
    def __init__(self, nthPrime):
        self.nthPrime = nthPrime

    # return the nth Prime number
    def GetPrime(self):

        nthPrime = self.nthPrime
        counter = 0
        i = 2

        while counter < nthPrime:
            bPrime = True
            j = 2

            while j < i:
                if i % j == 0:
                    bPrime = False
                    break
                else:
                    j = j + 1

            if bPrime is True:
                counter = counter + 1

            # Increase the number
            i = i + 1

            # if the next iteration does not finish the loop or
            # it is an even number then increase it to make it odd
            if counter < nthPrime and self.IsEven(i) is True:
                i = i + 1

        return i - 1





# Calculate the 10th prime number
MyPrime = CPrime()
    print(MyPrime.GetPrime(10))