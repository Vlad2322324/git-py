class Friends:
    connections = ()

    def __init__(self, connections):
        self.connections = set()
        for connection in connections:
            self.connections.add(frozenset(connection))
            print(f'+{connection}')

    def add(self, connection):
        self.connections.add(frozenset(connection))
        print(f'++{connection}')

    def remove(self, connection):
        self.connections.discard(frozenset(connection))
        print(f'-{connection}')

    def names(self):
        return set(name for connection in self.connections for name in connection)

    def connected(self, name):
        res = set()
        for connection in self.connections:
            if name in connection:
                res.update(connection)
        res.discard(name)
        return res


f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"e", "c"}))
print(f.names())  # {'b', 'c', 'a'}

f.add({"c", "d"})
print('Names:', f.names())

f.remove({"c", "a"})
print(f.names())

print('Дружат с C', f.connected("c"))
