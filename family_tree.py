class familymember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color 
        self.height_cm = height_cm
    def show_traits(self):
        print("eye color:", self.eye_color)
        print("height (cm):", self.height_cm)
class kid(familymember):
    def __init__(self, name, age , eye_color, height_cm):
        self.name = name
        self.age = age
        super(). __init__(eye_color,height_cm)
    def  show_traits(self):
        print("age:", self.age)
        print("age:", self.age)
        super().show_traits()
    def favorite_hobby(self,hobby):
        print(self.name, "loves", hobby)
child = kid ("maya", 10, "brown", 140)
child.show_traits()
child.favorite_hobby("drawing")
print("is kid a subclass of familymember?", issubclass(kid,familymember))



        