import abc

class Character(abc.ABC):
    def __init__(self, name, level=1, skill_points=0, *skills):
        self._name = name
        self._level = level
        self._skill_points = skill_points
        self.skills = list(skills)

    @abc.abstractmethod
    def clone(self):
        pass

    def learn_skill(self, skill):
        self.skills.append(skill)

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def skill_points(self):
        return self._skill_points

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, Skill Points: {self.skill_points}, Skills: {', '.join(self.skills)}"


class Mage(Character):
    def __init__(self, name, level=1, skill_points=0, *skills):
        super().__init__(name, level, skill_points, "Earthquake", *skills)

    def clone(self):
        return Mage(self.name, self.level, self.skill_points, *self.skills)

class Bard(Character):
    def __init__(self, name, level=1, skill_points=0, *skills):
        super().__init__(name, level, skill_points, "Moral support", *skills)

    def clone(self):
        return Bard(self.name, self.level, self.skill_points, *self.skills)

class Warrior(Character):
    def __init__(self, name, level=1, skill_points=0, *skills):
        super().__init__(name, level, skill_points, "Sword Throw", *skills)

    def clone(self):
        return Warrior(self.name, self.level, self.skill_points, *self.skills)

class Tank(Character):
    def __init__(self, name, level=1, skill_points=0, *skills):
        super().__init__(name, level, skill_points, "Raise shield", *skills)

    def clone(self):
        return Tank(self.name, self.level, self.skill_points, *self.skills)

# Should be able to clone heroes
mageLeo = Mage("Leo")
cloneMage = mageLeo.clone()

print(mageLeo, cloneMage)

bardLeo = Bard("Leo")
cloneBard = bardLeo.clone()

print(bardLeo, cloneBard)

warriorLeo = Warrior("Leo")
cloneWarrior = warriorLeo.clone()

print(warriorLeo, cloneWarrior)

tankLeo = Tank("Leo")
cloneTank = tankLeo.clone()

print(tankLeo, cloneTank)

# Should be able to have skills based on the class

print("Mage: ", mageLeo.skills)
print("Bard: ", bardLeo.skills)
print("Warrior: ", warriorLeo.skills)
print("Tank: ", tankLeo.skills)

# Should be able to learn new skills

mageLeo.learn_skill("Bad eye curse")

print("Mage with a new skill: ", mageLeo.skills)

# Should allow players to change the name of a clone

cloneTank._name = "Ruben"

print("Original tank: ", tankLeo.name)
print("Cloned tank: ", cloneTank.name)

# Should retain original Info

bardLeo._level = 30
bardLeo._skill_points = 25

newCloneBard = bardLeo.clone()

print("Original bard stats: ", bardLeo)
print("Clone bard stats: ", newCloneBard)
