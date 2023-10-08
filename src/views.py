from src import app

import json
import datetime
@app.route('/healthcheck')
def healthCheck():

    return json.dumps({
        'date': str(datetime.datetime.now()),
        'status': 'ok'
    })