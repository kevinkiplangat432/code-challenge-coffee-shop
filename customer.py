class Customer:
    def __init__(self, name):
        self._name = None
        self.name =name


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name= name

        else:
            print(f"invalid name: {name}, The name should be of 1 to 15 characters long, please try again")

    