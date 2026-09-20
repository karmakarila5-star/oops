class PetProfile:
    def __init__(self, name, animal_type, age, breed, weight, is_paid=False):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.breed = breed
        self.weight = weight
        self.is_paid = is_paid

    def display_profile(self):
        status = " Premium (Paid)" if self.is_paid else " Standard (Free)"
        print(f"\n--- Pet Profile: {self.name} ({status}) ---")
        print(f"Type:   {self.animal_type}")
        print(f"Breed:  {self.breed}")
        print(f"Age:    {self.age} years old")
        print(f"Weight: {self.weight} lbs")


def main():
    pet_database = []
    
    print("Welcome to the Paid Pet Profile Builder!")
    
    pet1 = PetProfile(name="Buddy", animal_type="Dog", age=3, breed="Golden Retriever", weight=70, is_paid=True)
    pet2 = PetProfile(name="Whiskers", animal_type="Cat", age=2, breed="Siamese", weight=10, is_paid=False)
    
    pet_database.append(pet1)
    pet_database.append(pet2)

    print("\n--- Create a New Pet Profile ---")
    name = input("Enter Pet Name: ")
    animal_type = input("Enter Animal Type (e.g., Dog, Cat, Bird): ")
    
    try:
        age = int(input("Enter Pet Age: "))
        weight = float(input("Enter Pet Weight (lbs): "))
    except ValueError:
        age, weight = 0, 0.0

    breed = input("Enter Pet Breed: ")
    
    pay_choice = input("Upgrade to Premium Paid Profile for ₹5? (yes/no): ").strip().lower()
    is_paid = pay_choice == 'yes'

    new_pet = PetProfile(name, animal_type, age, breed, weight, is_paid)
    pet_database.append(new_pet)

    print("\nRetrieving all profiles from database...")
    for pet in pet_database:
        pet.display_profile()

if __name__ == "__main__":
    main()