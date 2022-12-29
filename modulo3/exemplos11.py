
class Snake:
    def __init__(self):
        self.victims = 0

    def increment(self):
        self.victims += 1



s = Snake()
s.increment()

print(s.__dict__)