class Polynomial:
    def __init__(self):
        self.polynomial = []

    def insert(self, coef, exp):
        self.polynomial.append((coef, exp))

    def print_polynomial(self):
        for i in range(len(self.polynomial)):
            if i < len(self.polynomial) - 1:
                print(f"{self.polynomial[i][0]}x^{self.polynomial[i][1]} + ", end="")
            else:
                print(f"{self.polynomial[i][0]}x^{self.polynomial[i][1]}")


# Driver code
poly = Polynomial()
poly.insert(3, 2)
poly.insert(2, 1)
poly.insert(1, 0)

poly.print_polynomial()