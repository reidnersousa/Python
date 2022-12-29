# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))## cpoloco , na string
print("*".join(["omicron", "pi", "rho"]))## cpoloco * na string


# Demonstrating the lower() method:
print("SiGmA=60".lower())
print("SaaaS".upper())


# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))

print("pythoninstitute.org".lstrip(".org")) # remover o elemento que quer

print()
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
print()
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

print()
# Demonstrating the rfind() method:
# faz o mesmo que find so que começado da direita 'r'
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))



# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))


# Os loops startswith() .
# Demonstrating the startswith() method:
print("omega".startswith("meg"))   # verifica se uma determinada string começa com uma substring especificada
print("omega".startswith("om"))

print()


# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")


txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)


# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

print()

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

print()

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())
