class Classy:
    def __init__(self, value):
        self.var = value
        print("self.var",self.var)
        print("self",self)


obj_1 = Classy("object")

print("obj_1.var",obj_1.var)
