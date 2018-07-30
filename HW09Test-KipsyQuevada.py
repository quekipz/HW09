"""
Kipsy Quevada
SSW-810-WS: Special Topics in SSW
Summer 2018 | Professor Jim Rowland
Homework 08: Parameter, Modules, Files, Web
"""
#---------------------------------------------------------------------------



import unittest
from HW09KipsyQuevada import Repository #NOTE: does not work with dash or period in filename so they were deleted



#Test Suite
class RepositoryTest(unittest.TestCase):
    """ RepositoryTest class """
    def test__init__(self):
        """ test create_stud_pretty_tables function """
        results = list()
        results2 = list()
        results3 = list()
        rep = Repository("/Users/Class2018/Desktop/ssw810/GIT College Repository/HW09")
        for key, maj in rep.major_dict.items():
            dept, required, electives = maj.get_major_data()
            results3.append(dept)
            results3.append(required)
            results3.append(electives)
        self.assertEqual(results3, ['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], 'SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']])
        for stud in rep.student_list:
            cwid, name, major, course_list, remaining_list, electives_list = stud.get_student_data()
            results.append(cwid)
            results.append(name)
            results.append(major)
            results.append(course_list)
            results.append(remaining_list)
            results.append(electives_list)
        self.assertEqual(results, ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], '10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], '10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], '10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], '10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], '11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], '11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], '11658', 'Kelly, P', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], '11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], '11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], []])
        for inst in rep.instructor_list:
            for course_tally in inst.get_instructor_data():
                cwid, name, dept, course, students = course_tally
                results2.append(cwid)
                results2.append(name)
                results2.append(dept)
                results2.append(course)
                results2.append(students)
        self.assertEqual(results2, ['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4, '98765', 'Einstein, A', 'SFEN', 'SSW 540', 3, '98764', 'Feynman, R', 'SFEN', 'SSW 564', 3, '98764', 'Feynman, R', 'SFEN', 'SSW 687', 3, '98764', 'Feynman, R', 'SFEN', 'CS 501', 1, '98764', 'Feynman, R', 'SFEN', 'CS 545', 1, '98763', 'Newton, I', 'SFEN', 'SSW 555', 1, '98763', 'Newton, I', 'SFEN', 'SSW 689', 1, '98762', 'Hawking, S', 'SYEN', 'No Courses On Record', 'N/A', '98761', 'Edison, A', 'SYEN', 'No Courses On Record', 'N/A', '98760', 'Darwin, C', 'SYEN', 'SYS 800', 1, '98760', 'Darwin, C', 'SYEN', 'SYS 750', 1, '98760', 'Darwin, C', 'SYEN', 'SYS 611', 2, '98760', 'Darwin, C', 'SYEN', 'SYS 645', 1])


def main():
    unittest.main()




main()