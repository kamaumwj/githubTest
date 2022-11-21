class Animal:

    def __init__(self, AnimalType):
        self._type = AnimalType.lower()
        self._sound = ""

    # a getter funcion
    @property
    def type(self):
        return self._type

    # a setter function
    @type.setter
    def type(self, value):
        self._type = value

    def makenoise(self):
        if self._type == "herbivore":
            self._sound = "moo"
        elif self._type == "carnivore":
            self._sound = "Miawwwww"
        elif self._type == "bird":
            self._sound = "chip chip chip"
        return self._sound


an1 = Animal("Carnivore")

print(f'The animal type is {an1.type}')

## Change animal type
an1.type = "Herbivore"

print(f'The animal type is {an1.type}')


print(" This small-error-fix branch is done")