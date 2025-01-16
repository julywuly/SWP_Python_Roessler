class Auto:
    def __init__(self, ps):
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        raise TypeError("Addition is only supported between Car objects.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        raise TypeError("Subtraction is only supported between Car objects.")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        raise TypeError("Multiplication is only supported between Car objects.")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        raise TypeError("Comparison is only supported between Car objects.")

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        raise TypeError("Comparison is only supported between Car objects.")

    def __len__(self):
        return self.ps


if __name__ == "__main__":
    a1 = Auto(50)
    a2 = Auto(60)

    print(f"Addition: {a1 + a2}")

    print(f"Subtraction: {a2 - a1}")

    print(f"Multiplication: {a1 * a2}")

    print(f"Equal: {a1 == a2}")
    print(f"Kleiner als: {a1 < a2}")
    print(f"Größer als: {a2 > a1}")

    print(f"PS von a1 (Länge): {len(a1)}")

    try:
        print(a1 + 10)
    except TypeError as e:
        print(e)

    try:
        print(a1 - "Auto")
    except TypeError as e:
        print(e)

    try:
        print(a1 < 100)
    except TypeError as e:
        print(e)
