# Author: Ashlyn Musgrave
# Github Username: ashlyn-musgrave
# Date: 6/28/2023
# Description: This program finds the mean, median, and mode of students by importing the
#statistics module.

import statistics
class Student:
    """This class represents a student's information"""
    def __init__(self, name, grade):
        """This function initializes data members with argument values"""
        self._name = name
        self._grade = grade

    def get_grade(self):
        """This method returns the grade parameter"""
        return self._grade

def basic_stats(student):
    """This function takes as a parameter a list of Student objects and returns a
    tuple containing the mean, median, and mode"""
    total = []
    for x in student:
        total.append(x.get_grade())
        mean = statistics.mean(total)
        median = statistics.median(total)
        mode = statistics.mode(total)
        stats = (mean, median, mode)
    return stats
