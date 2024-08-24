class Alphabet:
    def __init__(self, s):
        self.s = s
    def countConsonants(self):
        count = 0
        string = self.s
        for letter in string:
            if letter.lower() not in "aeiou":
                count += 1
        print(count)

st = input("Enter a string: ")
s = Alphabet(st)
s.countConsonants()
