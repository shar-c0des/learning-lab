class Difference:
    def __init__(self, a):
        self.a = a

        self.maximumDifference = 0

    def computeDifference(self):
        max_val = max(self.a)
        min_val = min(self.a)
        self.maximumDifference = max_val - min_val


_ = input()
a = [int(e) for e in input().split()]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)