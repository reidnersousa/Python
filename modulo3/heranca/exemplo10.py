class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass

class Sub1(Right, Left):
    pass

obj = Sub()
obj1 = Sub1()

print(obj.var, obj.var_left, obj.var_right, obj.fun())
print(obj1.var, obj1.var_left, obj1.var_right, obj1.fun())
