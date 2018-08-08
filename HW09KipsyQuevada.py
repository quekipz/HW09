"""
Kipsy Quevada
SSW-810-WS: Special Topics in SSW
Summer 2018 | Professor Jim Rowland
Homework 09: Advanced Python Topics
"""
#---------------------------------------------------------------------------

#*********************
#IMPORTS
from prettytable import PrettyTable
import sqlite3
#*********************

#*********************
#ADDITIONAL FUNCTIONS

def file_reader(path, field_count, sep=',', header=False):
    """ read text files and return all of the values on a single line on each call to next() """
    first_line = True
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError("{} could not be opened.".format(path))
    else:
        with fp:
            for count, line in enumerate(fp):
                if header and first_line:
                    first_line = False
                    continue
                else:
                    new_line = line.strip()
                    line_list = new_line.split(sep)
                    if field_count != len(line_list):
                        count += 1 
                        raise ValueError("{} has {} field(s) on line {} but expected {}".format(path, len(line_list), count, field_count))
                    else:
                        yield line_list

#*********************



#*********************
#CLASSES

#Major Class
class Major:
    """ return the summary data about a single major needed in the pretty table """

    def __init__(self, major):
        """ initialize Student instance """
        self.major = major
        self.required_courses = list()
        self.electives = list()
    
    def get_major(self):
        """ return major name """
        return self.major

    def add_required_course(self, required):
        """ add required course from majors.txt """
        self.required_courses += [required]
    
    def add_elective(self, elective):
        """ add elective from majors.txt """
        self.electives += [elective]

    def get_required(self):
        """ get required courses from majors.txt """
        return self.required_courses

    def get_electives(self):
        """ get required electives from majors.txt """
        return self.electives

    def get_major_data(self):
        """" return major data in prettytable format """
        return [self.major, sorted(self.required_courses), sorted(self.electives)]

#Student Class
class Student:
    """ allow other classes to add a course and grade to the container of courses and grades and return the summary data about a single student needed in the pretty table """

    def __init__(self, cwid, name, major, remaining, electives):
        """ initialize Student instance """
        self.cwid = cwid
        self.name = name
        self.major = major
        self.course_grade_dict = {} # each key represents the course name; each value represents the grade for that course
        self.remaining_list = list(remaining)
        self.electives_list = list(electives)

    def add_course_and_grade(self, course, grade):
        """ add course and grade from grades.txt """
        self.course_grade_dict[course] = grade
        if grade in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']:
            if course in self.remaining_list:
                self.remaining_list.remove(course)
            elif course in self.electives_list:
                self.electives_list = []


    def get_student_data(self):
        """" return student data in prettytable format """
        return [self.cwid, self.name, self.major, sorted(self.course_grade_dict.keys()), sorted(self.remaining_list), sorted(self.electives_list)]


#Instructor Class
class Instructor:
    """ allow other classes to specify a course, and updates the container of courses taught to increment the number of students by 1 and return information needed by the Instructor prettytable. """

    def __init__(self, cwid, name, dept):
        """ initialize Instructor instance """
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.course_stud_dict = {} # each key represents the course name; each value represents the number of students enrolled

    def add_course_and_stud(self, course):
        """ add course and student count from grades.txt """
        # [self.course_stud_dict[course] += 1 if course in self.course_stud_dict else self.course_stud_dict[course] = 1]
        if course in self.course_stud_dict:
            self.course_stud_dict[course] += 1
        else:
            self.course_stud_dict[course] = 1

    def get_instructor_data(self):
        """ return instructor data in prettytable format """
        if self.course_stud_dict == {}:
            yield [self.cwid, self.name, self.dept, "No Courses On Record", "N/A"]
        else:
            for course, stud in self.course_stud_dict.items():
                yield [self.cwid, self.name, self.dept, course, stud]


#Repository Class
class Repository:
    """ read students.txt, instructors.txt, and grades.txt to print student and instructor prettytable """
    def __init__(self, dir_path):
        """ initialize Repository instance """
        self.dir_path = dir_path
        self.major_dict = {} # major name: major object
        self.student_list = list()
        self.instructor_list = list()
        self.grade_list = list()
        try:
            path = self.dir_path + '/' + "majors.txt"
            for major, flag, course in file_reader(path, 3, sep='\t', header=False):
                if major not in self.major_dict.keys():
                    self.major_dict[major] = Major(major)
                item1 = self.major_dict[major]
                if flag == 'R':
                    item1.add_required_course(course)
                else:
                    item1.add_elective(course)

            path = self.dir_path + '/' + "students.txt"
            for cwid, name, major in file_reader(path, 3, sep='\t', header=False):
                if major in self.major_dict.keys():
                    found_major = self.major_dict[major]
                    self.student_list.append(Student(cwid, name, major, found_major.get_required(), found_major.get_electives()))
                else:
                    raise SyntaxError("No corresponding major found in majors.txt")
            path = self.dir_path + '/' + "instructors.txt"
            for cwid, name, dept in file_reader(path, 3, sep='\t', header=False):
                self.instructor_list.append(Instructor(cwid, name, dept))
            path = self.dir_path + '/' + "grades.txt"
            for s_cwid, course, grade, i_cwid in file_reader(path, 4, sep='\t', header=False):
                for item in self.student_list:
                    if s_cwid == item.cwid:
                        item.add_course_and_grade(course, grade)
                for item2 in self.instructor_list:
                    if i_cwid == item2.cwid:
                        item2.add_course_and_stud(course)
        except FileNotFoundError:
            print("The directory", self.dir_path, "does not exist.")
        
    def create_maj_pretty_tables(self):
        """ create major pretty table """
        major_summary = PrettyTable(field_names=["Dept", "Required", "Electives"])
        for major, major_object in self.major_dict.items():
            dept, required, electives = major_object.get_major_data()
            if required == []:
                required = 'No Required Classes On Record'
            if electives == []:
                electives = 'No Electives On Record'
            major_summary.add_row([dept, required, electives])
        print ("Major Summary")
        print(major_summary)

    def create_stud_pretty_tables(self):
        """ create student pretty table """
        student_summary = PrettyTable(field_names=["CWID", "Name", "Major", "Completed Courses", "Remaining Required", "Remaining Electives"])
        for stud in self.student_list:
            cwid, name, major, course_list, remaining_list, electives_list = stud.get_student_data()
            if course_list == []:
                course_list = 'No Classes On Record'
            if remaining_list == []:
                remaining_list = 'None'
            if electives_list == []:
                electives_list = 'None'
            student_summary.add_row([cwid, name, major, course_list, remaining_list, electives_list])
        print ("Student Summary")
        print(student_summary)
    
    def create_inst_pretty_tables(self):
        """ create instructor pretty table """
        instructor_summary = PrettyTable(field_names=["CWID", "Name", "Dept", "Course", "Students"])
        for inst in self.instructor_list:
            for course_tally in inst.get_instructor_data():
                cwid, name, dept, course, students = course_tally
                instructor_summary.add_row([cwid, name, dept, course, students])
        print ("Instructor Summary")
        print(instructor_summary)



#*********************



#*********************
#MAIN FUNCTION

#PART 1:
def main():
    DB_FILE = "/Users/Class2018/Desktop/ssw810/HW11.db"
    instructor_list = list()
    db = sqlite3.connect(DB_FILE)
    query = """ select i.CWID, i.Name, i.Dept, g.Course, count(g.Course) as student_count
                from instructors i
                    left join grades g on i.CWID = g.Instructor_CWID
                group by i.CWID, i.Name, i.Dept, g.Course; """
    for row in db.execute(query):
        instructor_list.append(row)
    instructor_summary = PrettyTable(field_names=["CWID", "Name", "Dept", "Course", "Students"])
    for inst in instructor_list:
        cwid, name, dept, course, students = inst
        instructor_summary.add_row([cwid, name, dept, course, students])
    print ("Instructor Summary")
    print(instructor_summary)
#*********************

main()