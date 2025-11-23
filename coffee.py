class Coffee:
    def __init__(self, name ):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >3:
            self._name = name
        else:
            print(f"invalid name:{name}, The name should be more than 3 char long")

    