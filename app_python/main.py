'''The Sanic web application for showing the time in Moscow.'''

from datetime import datetime, timedelta, timezone

from sanic import Sanic
from sanic.response import text

app = Sanic('moscow-time-app')
moscow_tz = timezone(timedelta(hours=3))

@app.get("/")
async def report_time(_request):
    '''Returns the time in Moscow'''
    return text(datetime.now(tz=moscow_tz).strftime('%H:%M:%S'))


if __name__ == "__main__":
    app.run(debug=True, access_log=True)
