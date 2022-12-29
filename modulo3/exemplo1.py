# Test examples here.
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()

obj.other()

## to excetuando um metodo dentro de outro metodo. 