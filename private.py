class myclass:
    __privatevar = 17;
    def __privmeth(self):
      print("i 'm inside class myclass")
    def hellow(self):
      print("private variable value: ",myclass. __privatevar)
foo = myclass()
foo.helow()
foo.__privmeth