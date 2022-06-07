class Student:
    def __init__(self, name, grades):
        # self.id = last_used_id + 1
        # last_used_id += 1
        self.name = name
        self.grades = grades  # list of grades

    def calc_gpa(self):
        return sum(self.grades) / len(self.grades)
    
    def is_passing(self):
        return self.calc_gpa() >= 2.0


class BloomTechStudent(Student):
    def __init__(self, name, grades):
        super().__init__(name, grades)
        self.has_flexed = False
    
    def flex(self):
        self.has_flexed = True


s1 = BloomTechStudent('joe', [3.4, 2.7, 4.0])
s2 = BloomTechStudent('anne', [1.5, 0.6])
# print(s1.name, s1.is_passing())
# print(s2.name, s2.is_passing())
print(s1.has_flexed)
s1.flex()
print(s1.has_flexed)