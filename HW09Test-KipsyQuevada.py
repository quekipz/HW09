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
        rep = Repository("/Users/Class2018/Desktop/ssw810/HW09")
        for stud in rep.student_list:
            cwid, name, course_list = stud.get_student_data()
            results.append(cwid)
            results.append(name)
            results.append(course_list)
        self.assertEqual(results, ['10103', "Baldwin, C", ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], '10115', "Wyatt, X", ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], '10172', "Forbes, I", ['SSW 555', 'SSW 567'], '10175', "Erickson, D", ['SSW 564', 'SSW 567', 'SSW 687'], '10183', "Chapman, O", ['SSW 689'], '11399', "Cordova, I", ['SSW 540'], '11461', "Wright, U", ['SYS 611', 'SYS 750', 'SYS 800'], '11658', "Kelly, P", ['SSW 540'], '11714', "Morton, A", ['SYS 611', 'SYS 645'], '11788', "Fuller, E", ['SSW 540']])
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