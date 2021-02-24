from Program import Program
from programURL import PROGRAM_URLS
from typing import Dict
import json
import os


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
        code = c.course_code
        data[code] = dict()

        data[code]["name"] = c.name
        data[code]["code"] = c.course_code
        data[code]["program_code"] = program
        data[code]["description"] = c.description
        data[code]["exclusions"] = c.exclusions
        data[code]["prerequisites"] = c.prerequisites
        data[code]["co_requisites"] = c.co_requisites
        data[code]["prerequisites_for"] = c.is_a_prerequisite_for

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


def export_json():
    """Writes all program course data into specific JSON files associated 
    with their program title
    """

    for program in PROGRAM_URLS: 
        data = extract_data_single(program)

        fp = './coursedata' 
        filename = program + '.json'

        writeJSON(fp, filename, data)
