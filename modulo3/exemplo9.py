class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5



# A função chamada incIntsI() obtém um objeto de qualquer classe, digitaliza o
# seu conteúdo a fim de encontrar todos os atributos inteiros com nomes que comecem por i,
# e incrementa-os por um.
def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            print(val)
            if isinstance(val, int):
                print(">",val)
                setattr(obj, name, val + 1)


print("a",obj.__dict__)
incIntsI(obj)
print("um",obj.__dict__)
