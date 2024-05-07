class Mixin:
    def metodo_1(self):
        print("Esse método contém melhorias para a classe A")


class Heranca:
    def metodo_1(self):
        print("Metodo 1")

    def metodo_2(self):
        print("metodo 2")

    def metodo_3(self):
        print("metodo 3")


class A(Heranca, Mixin):
    pass


instance = A()
instance.metodo_1()

print(A.mro())

# Method resolution order (MRO) é usado na função super() para determinar a ordem de chamada dos métodos de uma classe
