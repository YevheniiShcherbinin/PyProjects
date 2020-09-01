class Triangle():
    def __init__(self, ab, bc, ac):
        self.ab = float(ab)
        self.bc = float(bc)
        self.ac = float(ac)

    def areaTriangle(self):
        s = (self.ab + self.bc + self.ac) // 2
        return ((s * (s - self.ab) * (s - self.bc) * (s - self.ac)) ** 0.5)

    def perimeterTriangle(self):
        p = (self.ab + self.bc + self.ac)
        return p

    def kindTriangle(self):
        if ab + bc <= ac or ab + ac <= bc or bc + ac <= ab:
            return print("Triangle not exist")
        elif ab != bc and ab != ac and bc != ac:
            return print("Versatile")
        elif ab * ab + bc * bc == ac * ac:
            return print("Rectangular")
        elif ab == bc == ac:
            return print("Equilateral")
        else:
            return print("Isosceles")

ab = int(input("AB = "))
bc = int(input("BC = "))
ac = int(input("AC = "))
t = Triangle(ab, bc, ac)
print("Area=", t.areaTriangle())
print("Perimeter=", t.perimeterTriangle())
print(t.kindTriangle())
