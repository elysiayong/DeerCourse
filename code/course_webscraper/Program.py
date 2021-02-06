from lxml import html
import requests
from typing import List 

from Course import _Course

"""
by Shivam Bhatoolaul
"""

PROGRAM_URLS = {
# "ANT": "http://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=1",
# "AST": "http://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=2",
# "BIO": "http://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=3",
# "HSC": "http://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=51",
# "CSC": "http://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=7", 
"CCT": "http://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=4"
}

# TODO: ADD REST OF COURSES

class Program:
    """
    A class to get info about courses in a program at UTM.

    === Public Attributes ===
    courses: the database containing the information about courses in the program.
    """
    courses = List[_Course]

    def __init__(self, program):
        """
        :param program: the program we are accessing data for.
        """

        if program in PROGRAM_URLS:
            self.courses = _get_list_of_courses(program)
            self._get_is_a_prerequisite_for_courses()
        else:
            self.courses = None
            print("Program isn't in database yet...")

    def _get_is_a_prerequisite_for_courses(self):
        """
        For every course in the program, get the courses that that
        course is a prerequisite  for...
        """
        for course1 in self.courses:
            for course2 in self.courses:
                if course1.course_code in course2.prerequisites:
                    course1.add_is_a_prerequisite_for(course2)

    def __repr__(self):
        """
        :return: str representation of the object in the console.
        """
        return str(self.courses)

    def pretty_print_every_course(self):
        """
        Print the full information for every course in the program.
        """
        for course in self.courses:
            print(course.title)
            print(course.description)
            print("")

    def get_courses(self):
        """
        Get the courses attribute of the program.
        """
        return self.courses

def _get_list_of_courses(program):
    """
    :param program: the program we are accessing data for.
    :return: list of courses in List[_Course] format.
    """

    # Directly access page:
    url = PROGRAM_URLS[program]
    page = requests.get(url)
    page_content = page.content

    """ 
    AS A BACKUP, IF WEBSITE EVER CHANGES, just grab the local HTML save of the CSC course-page
    -- this avoids accessing the web-page over and over.

    with open('//Users//shivambhatoolaul//Desktop//CSC Courses.txt', 'r') as web_page:
        page_content = web_page.read()
    """

    # Create html tree from web-page
    tree = html.fromstring(page_content)
    body = tree[1]

    # Go to section with course info
    content = body[3]

    # Get raw course info
    courses_raw = []
    current_course = None
    for element in content.xpath("./*"):
        if element.tag == 'p':
            current_course = element.text
        else:
            if element.tag == "span":
                if "normaltext" in element.classes:
                    courses_raw.append((current_course, element.text_content()))

    # Clean up courses in courses_raw into _Course objects
    courses = []
    for course in courses_raw:
        courses.append(_Course(course[0], course[1].split("\n")))
    return courses
