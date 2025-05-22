class A:
    print("a")

class B(A):
    def show(self):
        print("b")
    
class C(A):
    def show(self):
        print("c")

class D(B, C):
    pass

d = D()
print(D.__mro__)