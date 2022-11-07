# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        print("entrou no i ==3 ")
        break ## terminou ja 
        print("exec o break")
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        print("entro no i==3")
        continue ## ele nao excutar essa linha
        print("exec o continue ") 
    print("Inside the loop.", i)
    ### nao executo esse bloco todo
print("Outside the loop.")
