# Populating the DB - Webscraper
## Running Requests.py
You can call the functions `add_programs()` or `add_courses()` from the CLI, but it's better to run `Requests.py` itself since you might need to run those functions with conditions.

## Warning
Since all programs and courses will be added to the database, this program will take a significant amount of time to run. So please beware before immediately running it.

## Small Scale Testing
Executing `asyncio.run(add_programs())` won't take a long time, so it is recommended to run it first and leave it be. (Comment out when `programNames.json` is created)\
\
However, executing `asyncio.run(add_courses())` will take an extremely long time. If you just want a few programs with their courses in the DB,
go to `programURL.py` and uncomment code as needed:

1) Run `asyncio.run(add_programs())` in `Requests.py` first
2) Go to `programURL.py` and comment out unwanted programs
3) Run `asyncio.run(add_courses())` in `Requests.py`

Note: start the server from the backend for this to work.
