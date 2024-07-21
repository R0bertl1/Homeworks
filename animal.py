import random

class Animal:
    def __init__(self, name, lifespan, satiety=100, age=None):
        self.name = name
        self.lifespan = lifespan
        self.gender = random.choice(["male", "female"])

        self.age = random.randint(1, lifespan) if age is None else age
        self.satiety = satiety

    def add_satiety(self, satiety):
        self.satiety = max(min(self.satiety + satiety, 100), 0)

    def age_one_unit(self):
        self.age += 1

    def is_old(self):
        return self.age > self.lifespan

    def is_hungry(self):
        return self.satiety < 10

    def print_animal_info(self):
        print(f"  {self.name}: Age {self.age}, Satiety {self.satiety}, Gender {self.gender}")

class Species:
    def __init__(self, name, count, size, diet, habitat, lifespan):
        self.name = name
        self.size = size
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan

        self.total_animals = 0
        self.animals = []

        self.add_animals(count, satiety=100)

    def add_animal(self, satiety, age = None):
        self.total_animals += 1

        animal = Animal(
            name=f"{self.name}_{self.total_animals}",
            lifespan=self.lifespan,
            satiety=satiety,
            age=age
        )

        self.animals.append(animal)

    def add_animals(self, count, satiety, age=None):
        for _ in range(count):
            self.add_animal(satiety, age)

    def mate_animals(self, animal_1_num, animal_2_num):
        animal_1 = next((a for a in self.animals if a.name == f"{self.name}_{animal_1_num}"), None)
        animal_2 = next((a for a in self.animals if a.name == f"{self.name}_{animal_2_num}"), None)

        if not animal_1 or not animal_2:
            print("Unknown animals")
            return

        if animal_1.gender == animal_2.gender:
            print("Invalid genders")
            return

        if self.habitat == "water":
            if animal_1.satiety > 50 and animal_2.satiety > 50:
                self.add_animals(10, 23, 0)
            else:
                print("Can't mate")

        elif self.habitat == "air":
            if animal_1.satiety > 42 and animal_2.satiety > 42 and animal_1.age > 3 and animal_2.age > 3:
                self.add_animals(4, 64, 0)
            else:
                print("Can't mate")

        elif self.habitat == "land":
            if animal_1.satiety > 20 and animal_2.satiety > 20 and animal_1.age > 5 and animal_2.age > 5:
                self.add_animals(2, 73, 0)
            else:
                print("Can't mate")

    def simulate_time_unit_age(self):
        for animal in self.animals:
            animal.age_one_unit()

        new_food = 0

        for animal in self.animals:
            if animal.is_old():
                new_food = new_food + self.size
                print (f"{animal.name} dead due to old age")
        self.animals = [a for a in self.animals if not a.is_old()]

        return new_food

    def simulate_time_unit_hunt(self, plant_available, all_species):
        for animal in self.animals:
            old_satiety = animal.satiety

            if self.diet == "plant":
                plant_available = max(0, plant_available - 1)

                if plant_available == 0:
                    animal.add_satiety(-9)
                    print(f"{animal.name} no plant, satiety {old_satiety} -> {animal.satiety}")
                else:
                    animal.add_satiety(26)
                    print(f"{animal.name} plant, satiety {old_satiety} -> {animal.satiety}")
            else:
                diet_species = next(s for s in all_species if s.name == self.diet)

                if len(diet_species.animals) > 0:
                    if random.random() > 0.5:
                        animal_to_eat = random.choice(diet_species.animals)
                        diet_species.animals.remove(animal_to_eat)
                        animal.add_satiety(53)
                        print(f"{animal.name} eated {animal_to_eat.name}, satiety {old_satiety} -> {animal.satiety}")
                    else:
                        animal.add_satiety(-16)
                        print(f"{animal.name} failed to catch, satiety {old_satiety} -> {animal.satiety}")
                else:
                    animal.add_satiety(-9)
                    print(f"{animal.name} no species {self.diet}, satiety {old_satiety} -> {animal.satiety}")

        return plant_available

    def simulate_time_unit_hunger(self):
        new_food = 0

        for animal in self.animals:
            if animal.is_hungry():
                new_food = new_food + animal.size
                print(f"{animal.name} dead due to hunger")

        self.animals = [a for a in self.animals if not a.is_hungry()]

        return new_food

    def print_species_info(self):
        print(f"{self.name}: Diet {self.diet}, Habitat {self.habitat}, Lifespan {self.lifespan}, Size: {self.size}")

    def print_animals_info(self):
        for animal in self.animals:
            animal.print_animal_info()

class Ecosystem:
    def __init__(self):
        self.species = []
        self.plant_food = 1000  # initial plant food

        # Add some initial animals
        for i in range(12):
            species = Species(
                name=f"Species_{i+1}",
                count=random.randint(1, 10),
                size=random.randint(1, 100),
                diet=random.choice(["plant"] + [f"Species_{i+1}" for i in range(12)]),
                habitat=random.choice(["water", "land", "air"]),
                lifespan=random.randint(1, 20)
            )

            self.species.append(species)

    def add_animals(self, species_num, animal_count):
        species = next((s for s in self.species if s.name == f"Species_{species_num}"), None)
        if species:
            species.add_animals(animal_count, 100)
        else:
            print("Unknown species")

    def increase_plant_food(self, amount):
        self.plant_food += amount

    def simulate_time_unit(self):
        # step 1
        for species in self.species:
            self.plant_food = self.plant_food + species.simulate_time_unit_age()
        # step 2
        for species in self.species:
            self.plant_food = species.simulate_time_unit_hunt(self.plant_food, self.species)
        # step 3
        for species in self.species:
            self.plant_food = self.plant_food + species.simulate_time_unit_hunger()
    def mate_animals(self, species_num, animal_1_num, animal_2_num):
        species = next((s for s in self.species if s.name == f"Species_{species_num}"), None)
        if species:
            species.mate_animals(animal_1_num, animal_2_num)
        else:
            print("Unknown species")

    def print_species(self):
        for species in self.species:
            species.print_species_info()
        print(f"Plant food: {self.plant_food}")

    def print_animals(self):
        for species in self.species:
            species.print_species_info()
            species.print_animals_info()
        print(f"Plant food: {self.plant_food}")

ecosystem = Ecosystem()

ecosystem.print_species()

while True:
    print ("Enter:")
    print ("a - to add animal")
    print ("f - to add food")
    print ("p - to print animals")
    print ("m - to mate animals")
    print ("t - to simulate 1 time unit")
    print ("q - exit")

    command = input()

    if command == "a":
        print ("Enter species num:")
        species_num = int(input())
        
        print ("How many animals to add:")
        animal_count = int(input())

        ecosystem.add_animals(species_num, animal_count)

    elif command == "f":
        print ("Enter how much food to add:")
        food = int(input())
        ecosystem.increase_plant_food(food)

    elif command == "p":
        ecosystem.print_animals()

    elif command == "m":
        print ("Enter species num:")
        species_num = int(input())

        print ("Enter 1st animal num:")
        animal_1_num = int(input())

        print ("Enter 2nd animal num:")
        animal_2_num = int(input())

        ecosystem.mate_animals(species_num, animal_1_num, animal_2_num)

    elif command == "t":
        ecosystem.simulate_time_unit()

    elif command == "q":
        quit()












