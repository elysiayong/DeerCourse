from typing import List
import textwrap

"""
by Shivam Bhatoolaul
"""

class _Course:
    """
    A private class to store info about a course at UTM.

    === Public Attributes ===
    title: the complete title of the course
    _course_code: just the course code for the course.
    description: the course description.
    exclusions: the course(s) that make you ineligible to take this course.
    prerequisites: the course(s) needed to take this course.
    co_requisites: the course(s) you need to take at the same time as this course.
    is_a_prerequisite_for: the courses(s) that have this course as a prerequisite.
    """

    title: str
    course_code: str
    description: str
    exclusions: str
    prerequisites: str
    co_requisites: str
    is_a_prerequisite_for: List[str]

    def __init__(self, title, list_of_information):
        """
        :param title: the course title.
        :param list_of_information: the list of information containing the rest
        of the attributes to set for course.
        """
        self.title = title
        self.course_code = title.split(" ")[0].upper()
        self.description = "\n".join(textwrap.wrap(list_of_information[1], 100))

        self.exclusions = ""
        self.prerequisites = ""
        self.co_requisites = ""
        # now use <self._get_exclusions_and_requisites()> to get the information above...
        self._get_exclusions_and_requisites(list_of_information)
        # we won't know this info down below until we have a full list of the other courses in the program.
        self.is_a_prerequisite_for = []

    def add_is_a_prerequisite_for(self, course):
        """
        Add a <course> that has this course as a prerequisite to
        <self.is_a_prerequisite_for>
        """
        self.is_a_prerequisite_for.append(course)

    def _get_exclusions_and_requisites(self, list_of_information):
        """
        A private method to set the exclusions, prerequisites and co-requisites of the course
        from :param list_of_information.
        """
        for info in list_of_information:
            if "Exclusion:" in info:
                self.exclusions = "\n".join(textwrap.wrap(info, 100))
            if "Prerequisite:" in info:
                self.prerequisites = "\n".join(textwrap.wrap(info, 100))
            if "Corequisite:" in info:
                self.co_requisites = "\n".join(textwrap.wrap(info, 100))

    def __repr__(self):
        """
        :return: str representation of the course in the console.
        """
        return self.course_code
