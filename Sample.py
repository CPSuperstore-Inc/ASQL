from ASQL import ASQL


class Bob:
    def __init__(self, age):
        self.age = age


a = ASQL([Bob(5), Bob(6), Bob(7), Bob(8)])
print(a.filter())

print(a.avg("age", "age"))
