##Robert Fernandez
##Complete
##This program will prompt the user to enter their pets name, type, and age and then display the information in a sentence.

#Prompt user to enter their pets name, type, and age
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


 ##Display the information in a sentence.       
def main():
    name = input("Enter the name of your pet: ")
    animal_type = input("Enter the type of animal your pet is: ")
    age = input("Enter the age of your pet: ")

    pet = Pet(name, animal_type, age)

    print("\nPet details:")
    print(f"Name: {pet.get_name()}")
    print(f"Type: {pet.get_animal_type()}")
    print(f"Age: {pet.get_age()}")
    
##call the main function
if __name__ == "__main__":
    main()
