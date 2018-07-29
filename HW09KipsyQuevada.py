"""
Kipsy Quevada
SSW-810-WS: Special Topics in SSW
Summer 2018 | Professor Jim Rowland
Homework 09: Advanced Python Topics
"""
#---------------------------------------------------------------------------

#*********************
#IMPORTS
import unittest
from prettytable import PrettyTable
import os
import sys
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

#Student Class
class Student:
    """ allow other classes to add a course and grade to the container of courses and grades and return the summary data about a single student needed in the pretty table """

    def __init__(self, cwid, name, major):
        """ initialize Student instance """
        self.cwid = cwid
        self.name = name
        self.major = major
        self.course_grade_dict = {} # each key represents the course name; each value represents the grade for that course
    
    def add_course_and_grade(self, course, grade):
        """ add course and grade from grades.txt """
        self.course_grade_dict[course] = grade

    def get_student_data(self):
        """" return student data in prettytable format """
        return [self.cwid, self.name, sorted(self.course_grade_dict.keys())]


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
        self.student_list = list()
        self.instructor_list = list()
        try:
            path = self.dir_path + '/' + "students.txt"
            for cwid, name, major in file_reader(path, 3, sep='\t', header=False):
                self.student_list.append(Student(cwid, name, major))
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
        
    def create_stud_pretty_tables(self):
        """ create student pretty table """
        student_summary = PrettyTable(field_names=["CWID", "Name", "Completed Courses"])
        for stud in self.student_list:
            cwid, name, course_list = stud.get_student_data()
            if course_list == []:
                course_list = 'No Classes On Record'
            student_summary.add_row([cwid, name, course_list])
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
    # unittest.main()
    stevens = Repository("/Users/Class2018/Desktop/ssw810/HW09") # read files and generate prettytables
    stevens.create_stud_pretty_tables()
    stevens.create_inst_pretty_tables()
#*********************



main()  