from lxml import html
import requests
from typing import List, Dict
import os
import json

from programURL import PROGRAM_URLS
from programURL import DEPT_URL


programs = Dict

def create_json():
    """
    Create programNames.py containing a dictionary of programs and their names
    """

    fp = "programNames.json"
    try: 
        with open(fp, 'w+') as f:
            program_names = _get_program_desc()
            json.dump(program_names, f, indent=2)

    except Exception as e:
        print(e)
        raise


def _get_program_desc():
    """
    assert: len(PROGRAM_URLS.keys()) == len(a)
    :return: dictionary of programs.
    """
    page = requests.get(DEPT_URL)

    # Get html
    tree = html.fromstring(page.content)
    a = tree.xpath("//div[@class='contentpos']//a")

    program_keys = list(PROGRAM_URLS.keys())
    program_names = dict()

    for index in range(len(program_keys)):
        code = program_keys[index]
        name = a[index].text

        program_names[code] = dict()
        program_names[code]["code"] = code
        program_names[code]["name"] = name

    return program_names
