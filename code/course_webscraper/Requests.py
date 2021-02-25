import ScrapeCourses
import ScrapePrograms
import httpx, asyncio, json
import os, glob
from typing import Dict
from time import time


async def _task(URL, data, verbose):
    start = time()

    timeout = httpx.Timeout(connect=(60*3), read=60, write=(60*3), pool=60)
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(URL, data=data)

        if verbose:
            print("request duration: ", time() - start)
            print(response)
            print(response.text)
            print('--------------------------------------------')
    return response


async def _post(URL, data, verbose):
    tasks = []
    for item in data:
        tasks.append(_task(URL, json.dumps(data[item]), verbose))
    await asyncio.gather(*tasks)
    

async def add_programs(verbose=False):
    URL = "http://localhost:8080/admin/programs/{program_code}"

    # Parse json
    with open('./course_webscraper/programNames.json', 'r') as f:
        data = json.load(f)

    await _post(URL, data, verbose)


async def add_courses(verbose=False):
    URL = "http://localhost:8080/admin/courses/{course_code}"

    fp = './coursedata'

    # Parse all json files in coursedata
    for filename in glob.glob(os.path.join(fp, '*.json')):
        with open(filename, 'r') as f:
            data = json.load(f)

        await _post(URL, data, verbose)


def populate_db(createJSON=True, verbose=False):
    start = time()
    loop = asyncio.get_event_loop()

    # scrape programs and courses
    if createJSON:
        ScrapePrograms.create_json()
        ScrapeCourses.create_json()

    # set verbose=True if you want to see server responses or for debugging purposes
    loop.run_until_complete(add_programs(verbose=verbose))
    loop.run_until_complete(add_courses(verbose=verbose))
    print("request duration: ", time() - start)


# NOTE: Please read the README.md on webscraper before running this code, add parameters as necessary
if __name__ == "__main__":    
    populate_db()




    