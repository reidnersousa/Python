import os

### Criação de diretoria recursiva

os.makedirs("my_first_directory/my_second_directory")
print(os.listdir())

os.chdir("my_first_directory")
print(os.listdir())
