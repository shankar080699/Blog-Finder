from flask import Flask, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
import numpy as np
import json
import pandas as pd
import numpy as np
import blog as bg

app = Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# CORS(app, resources={r"/api": {"origins": "*"}})

@app.route('/blogs', methods=['POST'])
# @crossdomain(origin="*", headers=["Content-Type"])
def blogs():
    tle = request.json.get('title')
    print(tle)
    data = bg.blogs(tle)	
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
    