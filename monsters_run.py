## import from all


from monsters_monster import *
from student_monster import *
from monster_course import *

print("Welcome to Monsters Inc. University! Ready to learn?")

#create two student objects

tytus = student_monster('Tytus', '223', 'blue', '0001', ['fast', 'strong'])
leandro = student_monster('Leandro', '118', 'yellow', '0002', ['funny', 'smart'])

# add a skill to each of my students

tytus.add_skill('super laugh')
leandro.add_skill('hadouken!')




# create a course i.e. initialize a course

scary_tickle_course = monster_course('tickling 101', '02.02.2021')




#enrolling tytus and leandro into tickle course

scary_tickle_course.add_student(tytus)
scary_tickle_course.add_student(leandro)




# EXTRA - get the list of students, iterate over it and print the students name