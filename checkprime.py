class CheckPrime:
    def __init__(self, n):
        self.n = n
    def isprime(self):
        number = self.n
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is NOT prime!")
                break
        else:
            print(f"{number} is prime!")

n = int(input("Enter a number: "))
num = CheckPrime(n)
num.isprime()
