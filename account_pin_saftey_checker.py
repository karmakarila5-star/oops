class Account:
    def __init__(self, pin):
        self.__pin = pin

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if len(str(new_pin)) == 4:
            self.__pin = new_pin
        else:
            print("Invalid PIN")

    def __str__(self):
        return "This is an account"


acc = Account(1234)
print(acc)

try:
    print(acc.__pin)
except AttributeError:
    print("Private variable error")

acc.set_pin(5678)
print(acc.get_pin())