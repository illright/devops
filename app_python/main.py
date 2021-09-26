'''The Sanic web application for showing the time in Moscow.'''

import os
from datetime import datetime, timedelta, timezone

from sanic import Sanic
from sanic.response import text

app = Sanic('moscow-time-app')
moscow_tz = timezone(timedelta(hours=3))

VISITS_FILENAME = 'visits.txt'

@app.get("/")
async def report_time(_request):
    '''Returns the time in Moscow'''

    if not os.path.exists(VISITS_FILENAME):
        with open(VISITS_FILENAME, 'w', encoding='utf-8'):
            pass

    with open(VISITS_FILENAME, 'r+', encoding='utf-8') as visits_file:
        last_visits = int(visits_file.read() or 0)
        visits_file.seek(0)
        visits_file.write(str(last_visits + 1))

    return text(datetime.now(tz=moscow_tz).strftime('%H:%M:%S'))

@app.get("/visits")
async def report_visits(_request):
    '''Returns the amount of visits to the root of the website.'''

    if os.path.exists(VISITS_FILENAME):
        with open(VISITS_FILENAME, 'r', encoding='utf-8') as visits_file:
            return text(visits_file.read())
    else:
        return text('0')


if __name__ == "__main__":
    app.run(debug=True, access_log=True)
