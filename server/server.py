from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_sensor_data')
def get_sensor_data():
    response = jsonify({
        'result': util.get_sensor_data()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_rainfall', methods=['GET', 'POST'])
def predict_rainfall():
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])

    response = jsonify({
        'estimated_rainfall': util.get_estimated_rainfall(temperature, humidity)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting the python flask server to predict rainfall...")
    util.load_saved_artifacts()
    app.run()
