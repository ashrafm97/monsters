
# need student_id and a skill_list

from monsters_monster import *

class student_monster(Monster):
    def __init__(self, name, tax_number, fur_colour, student_numb, skill_list = None):
        if skill_list is None:
            skill_list = []
        self.__student_numb = student_numb
        self.skill_list = skill_list

    def set_student_numb(self, student_numb):
        self.__student_numb = student_numb

    def get_student_numb(self):
        return self.__student_numb

    def add_skill(self, new_skill):
        self.skill_list.append(new_skill)

    def get_skills_list(self):
        return ', '.join(self.skill_list)

