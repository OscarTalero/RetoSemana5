class Queue:
    def __init__(self):
        self.items = []
 
    def vacia(self):
        return self.items == []
 
    def entrar(self, item):
        self.items.insert(0,item)
 
    def sacar(self):
        return self.items.pop()
 
    def longitud(self):
        return len(self.items)