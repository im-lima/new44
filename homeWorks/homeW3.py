class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value + other.value)
        return Calculator(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value - other.value)
        return Calculator(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value * other.value)
        return Calculator(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value / other.value)
        return Calculator(self.value / other)

    def __str__(self):
        return str(self.value)

calc1 = Calculator(10)
calc2 = Calculator(20)

result_add = calc1 + calc2
result_sub = calc1 - calc2
result_mul = calc1 * calc2
result_div = calc1 / calc2

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")
print(f"Division: {result_div}")