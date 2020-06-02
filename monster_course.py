# # sudo code
# # so need to create a course name, list_of_students and also a start date...
# this doesnt have to be anything crazy, I think random ints will do...


class monster_course():
    def __init__(self, course_name, start_date, list_of_students=[]):
        self.__course_name = course_name
        self.start_date = start_date
        self.list_of_students = list_of_students
    ## to encapsulate the data is good practice here as you dont want a mishmash of names as the user wishes

    def set_course_name(self, course_name):
        self.__course_name = course_name.title()
# we are adding title incase its something like marine biology etc... need a capital
    def get_course_name(self):
        return self.__course_name

    def add_student(self, student):
        self.list_of_students.append(student)
        return 'Added student'
    def get_students(self):
        return ', '.join(self.__get_names())


    def __get_names(self):
        all_students = []
        for student in self.list_of_students():
            all_students.append(student.get_name())
        return all_students
    # def start_date(self, start_date):
    #     self.start_date() = start_date
    # def list_of_students(self, list_of_students):
    #     self.list_of_students() = list


## adding student on course