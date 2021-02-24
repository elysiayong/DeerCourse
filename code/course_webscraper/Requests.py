import ScrapeCourses
import ScrapePrograms
import httpx, asyncio, json
import os, glob
from typing import Dict
from time import time


async def _task(URL, data, verbose):
    start = time()

    async with httpx.AsyncClient() as client:
        response = await client.post(URL, data=data)

        if verbose:
            print("request duration: ", time() - start)
            print(response)
            print(response.text)
            print('--------------------------------------------')
    return response


async def _post(URL, data, verbose):
    for item in data:
        response = await _task(URL, json.dumps(data[item]), verbose)


async def add_programs(verbose=False):
    # Create programNames.json
    ScrapePrograms.create_json()

    URL = "http://localhost:8080/admin/programs/{program_code}"

    # Parse json
    with open('./course_webscraper/programNames.json', 'r') as f:
        data = json.load(f)

    await _post(URL, data, verbose)


async def add_courses(verbose=False):
    # Create course json files in coursedata
    ScrapeCourses.export_json()

    URL = "http://localhost:8080/admin/courses/{course_code}"

    fp = './coursedata'

    # Parse all json files in coursedata
    for filename in glob.glob(os.path.join(fp, '*.json')):
        with open(filename, 'r') as f:
            data = json.load(f)

        await _post(URL, data, verbose)


# NOTE: Please read the README.md on webscraper before running this code, uncomment as necessary
if __name__ == "__main__":    
    # set verbose=True if you want to see server responses or for debugging purposes
    asyncio.run(add_programs(verbose=True))
    asyncio.run(add_courses(verbose=True))




    