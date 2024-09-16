class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
            raise ValueError("Capacity has to be an integer")
        if capacity < 0:
            raise ValueError("Capacity has a non-negative integer")

        self.max = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n > self.max:
            raise ValueError(f"Too much cookies. Current capacity: {self.cookies}/{self.capacity}")

        self.cookies += int(n)

    def withdraw(self, n):
        if self.cookies - n < 0:
            raise ValueError(f"Insufficient cookies. Current capacity: {self.cookies}/{self.capacity}")

        self.cookies -= int(n)

    @property
    def capacity(self):
        return self.max

    @property
    def size(self):
        return self.cookies