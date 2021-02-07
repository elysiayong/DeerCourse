from Program import Program
from programURL import PROGRAM_URLS
from typing import Dict
import json
import os

"""
by Shivam Bhatoolaul & Elysia Monde Zhi Yong
"""

def extract_data_all(programs) -> Dict:
    """Extracts the data collected from creating Program objects from key-values 
    in parameter 'programs' and format it into a Dict

    programs : Dict
    returns : A Dict containing all programs with their respective course
    datas
    """

    data = dict()

    for p in programs.keys():

        program = Program(p)
        courses = program.get_courses()
        data[p] = dict()

        for c in courses:
            title = c.title
            data[p][title] = dict()

            data[p][title]["description"] = c.description
            data[p][title]["exclusions"] = c.exclusions
            data[p][title]["prerequisites"] = c.prerequisites
            data[p][title]["co_requisites"] = c.co_requisites
            data[p][title]["prerequisite_for"] = c.is_a_prerequisite_for

    return data


def extract_data_single(program) -> Dict:
    """Extracts the data collected from creating a single Program object from
    program and format it into a Dict

    program : str
    returns : A Dict containing the course data of program
    """

    data = dict()

    p = Program(program)
    courses = p.get_courses()

    for c in courses:
        title = c.title
        data[title] = dict()

        data[title]["description"] = c.description
        data[title]["exclusions"] = c.exclusions
        data[title]["prerequisites"] = c.prerequisites
        data[title]["co_requisites"] = c.co_requisites
        data[title]["prerequisite_for"] = c.is_a_prerequisite_for

    return data


def writeJSON(fp, filename, data):
    """Writes data into a JSON file format into the file path 'fp' with 
    the file name as 'filename'. If the file path does not exist, create
    the folder/file respectively


    fp : str
    filename : str
    data : Dict
    """

    if not os.path.exists(fp):
        try: 
            os.makedirs(fp)
        except Exception as e:
            print(e)
            raise
    
    with open(os.path.join(fp, filename), 'w') as outfile:
        json.dump(data, outfile, indent=4)


def export_multi_json():
    """Writes all program course data into specific JSON files associated 
    with their program title
    """

    for program in PROGRAM_URLS: 
        data = extract_data_single(program)

        fp = './coursedata' 
        filename = program + '.json'

        writeJSON(fp, filename, data)


def export_single_json():
    """Writes all program course data into a single JSON file
    """

    data = extract_data_all(PROGRAM_URLS)

    with open('program_data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == "__main__":

    # Uncomment the code below if you want single JSON file for each program
    # it wil be put into a folder called "coursedata"
    export_multi_json()

    # Uncomment the code below if you want a JSON file containing data for 
    # ALL programs, it will be written to program_data.json
    # export_single_json()
