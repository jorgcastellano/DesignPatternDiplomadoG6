import abc

class Character(abc.ABC):
    def __init__(self, name, level=1, skill_points=0, skills = []):
        self._name = name
        self._level = level
        self._skill_points = skill_points
        self.skills = skills

    @staticmethod
    @abc.abstractmethod
    def clone(self):
        pass

    def learnSkill(self, skill):
        self.skills.append(skill)
    
    def __str__(self):
        return f"Name: {self._name}, Level: {self._level}, Skill Points: {self._skill_points}, Skills: {self.skills}"


class Mage(Character):
    def __init__(self, name, level=1, skill_points=0, skills = ["Earthquake"]):
        super().__init__(name, level, skill_points)
        self.skills = skills

    def clone(self):
        return Mage(self._name, self._level, self._skill_points)
    

class Bard(Character):
    def __init__(self, name, level=1, skill_points=0, skills = ["Moral support"]):
        super().__init__(name, level, skill_points)
        self.skills = skills

    def clone(self):
        return Bard(self._name, self._level, self._skill_points)
    
class Warrior(Character):
    def __init__(self, name, level=1, skill_points=0, skills = ["Sword Throw"]):
        super().__init__(name, level, skill_points)
        self.skills = skills

    def clone(self):
        return Warrior(self._name, self._level, self._skill_points)
    

class Tank(Character):
    def __init__(self, name, level=1, skill_points=0, skills = ["Raise shield"]):
        super().__init__(name, level, skill_points)
        self.skills = skills

    def clone(self):
        return Tank(self._name, self._level, self._skill_points)

# Should be able to clone heroes
mageLeo = Mage("Leo");
cloneMage = mageLeo.clone();

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

mageLeo.learnSkill("Bad eye curse")

print("Mage with a new skill: ", mageLeo.skills)

# Should allow players to change the name of a clone

cloneTank._name = "Ruben";

print("Original tank: ", tankLeo._name)
print("Cloned tank: ", cloneTank._name)

# Should retain original Info

bardLeo._level = 30
bardLeo._skill_points = 25

newCloneBard = bardLeo.clone()

print("Original bard stats: ", bardLeo)
print("Clone bard stats: ", newCloneBard)