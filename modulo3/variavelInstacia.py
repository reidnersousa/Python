class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass(1)

example_object_2 = ExampleClass(2)


example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5
example_object_3.oo=10

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# Os objetos Python, quando criados, são dotados de um pequeno conjunto de propriedades 
# e métodos pré-definidos. Cada objeto tem-nos, quer os queira ou não. 
# Um deles é uma variável chamada __dict__ (é um dicionário).

# A variável contém os nomes e valores de todas as propriedades (variáveis) que o objeto 
# carrega atualmente. Vamos utilizá-la para apresentar o conteúdo de um objeto em segurança.


### privado

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
