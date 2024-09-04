from flask import Flask, jsonify, abort
from dotenv import load_dotenv
from waitress import serve 
import os
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

load_dotenv()

days = [
    {"id": 1, "name": "Monday"},
    {"id": 2, "name": "Tuesday"},
    {"id": 3, "name": "Wednesday"},
    {"id": 4, "name": "Thursday"},
    {"id": 5, "name": "Friday"},
    {"id": 6, "name": "Saturday"},
    {"id": 7, "name": "Sunday"},
]

app = Flask(__name__)
port = int(os.getenv("PORT", default=5000))



@app.route("/", methods=["GET"])
def get_days():
    logging.info('This is an info message:'days)
    return jsonify(days)


@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in days if day["id"] == day_id]
    if len(day) == 0:
        abort(404)
        logging.error('This is a error message',day)
    return jsonify({"day": day[0]})


@app.route("/", methods=["POST"])
def post_days():
    return jsonify({"success": True}), 201


if __name__ == "__main__":
    port = os.getenv('PORT')
    logging.warning('This is a warning message')
    serve(app,host="0.0.0.0",port=port, url_scheme='https')
