'''The Sanic web application for showing the time in Moscow.'''

import os
from datetime import datetime, timedelta, timezone

from sanic import Sanic
from sanic.response import text

app = Sanic('moscow-time-app')
moscow_tz = timezone(timedelta(hours=3))

visits_filename = 'visits.txt'

@app.get("/")
async def report_time(_request):
    '''Returns the time in Moscow'''

    if not os.path.exists(visits_filename):
        open(visits_filename, 'w').close()

    with open(visits_filename, 'r+') as visits_file:
        last_visits = int(visits_file.read() or 0)
        visits_file.seek(0)
        visits_file.write(str(last_visits + 1))

    return text(datetime.now(tz=moscow_tz).strftime('%H:%M:%S'))

@app.get("/visits")
async def report_time(_request):
    '''Returns the amount of visits to the root of the website.'''

    if os.path.exists(visits_filename):
        with open(visits_filename, 'r') as visits_file:
            return text(visits_file.read())
    else:
        return text('0')


if __name__ == "__main__":
    app.run(debug=True, access_log=True)
