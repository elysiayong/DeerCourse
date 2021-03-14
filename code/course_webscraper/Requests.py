import ScrapeCourses
import ScrapePrograms
import httpx, asyncio, json
import os, glob
from typing import Dict
from time import time

MAX_CONNECTIONS = 3


async def _task(URL, data, verbose, client):
    start = time()
    response = await client.put(URL, json=data)
    allowed_codes = [200, 409, 500]

    if response.status_code == 409 and "course" in URL:
        # Collision happened, need to merge programs and send updated info
        if verbose:
            print("course collision for course", data["code"])
        programs_codes_on_server = [x["code"] for x in response.json()["programs"]]
        new_data = {"program_codes": data["program_codes"] + programs_codes_on_server}
        response = await client.post(f"{URL}{data['code']}", json=new_data)
    if response.status_code not in allowed_codes:
        error_msg = f"Request failed with code {response.status_code}\n" + \
                    f"Sent data:{data}"
        if response.headers.get('content-type') == 'application/json':
            error_msg += f"\nResponse:{response.json()}"
        raise Exception(error_msg)


    if verbose:
        print("request duration: ", time() - start)
        print(response)
        print(response.text)
        print('--------------------------------------------')
    return response


async def _post(URL, data, verbose, connections=1):
    tasks = []
    timeout = httpx.Timeout(connect=(60 * 3), read=60, write=(60 * 3), pool=60)
    limits = httpx.Limits(max_connections=connections, max_keepalive_connections=connections-1)
    client = httpx.AsyncClient(timeout=timeout, limits=limits)
    async with client:
        for item in data:
            tasks.append(_task(URL, data[item], verbose, client))
        await asyncio.gather(*tasks)
    

async def add_programs(verbose=False):
    URL = "http://localhost:8080/admin/programs/"

    # Parse json
    with open('programNames.json', 'r') as f:
        data = json.load(f)

    await _post(URL, data, verbose)


async def add_courses(verbose=False):
    URL = "http://localhost:8080/admin/courses/"

    fp = 'coursedata'

    # Parse all json files in coursedata
    for filename in glob.glob(os.path.join(fp, '*.json')):
        with open(filename, 'r') as f:
            data = json.load(f)

        await _post(URL, data, verbose, connections=MAX_CONNECTIONS)


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



    