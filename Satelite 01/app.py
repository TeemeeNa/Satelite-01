from flask import Flask, render_template, jsonify, send_from_directory
from datetime import datetime

app = Flask(__name__)

# Mock Data for Bangkok Canals (until real APIs are integrated)
MOCK_STATIONS = [
    {
        "id": "st-1",
        "name": "Khlong Saen Saep (Pratunam)",
        "lat": 13.7499,
        "lng": 100.5407,
        "source": "Bangkok Metropolitan Administration (Mock)",
        "timestamp": datetime.now().strftime("%d %b %Y, %H:%M"),
        "data": {
            "ph": 6.8,
            "do": 3.2,
            "temperature": 29.5,
            "turbidity": 45,
            "waste_detection": {
                "status": "Possible waste accumulation detected",
                "confidence": 85,
                "timestamp": datetime.now().strftime("%d %b %Y, %H:%M")
            }
        }
    },
    {
        "id": "st-2",
        "name": "Khlong Phadung Krung Kasem",
        "lat": 13.7329,
        "lng": 100.5168,
        "source": "BMA Environmental Dept (Mock)",
        "timestamp": datetime.now().strftime("%d %b %Y, %H:%M"),
        "data": {
            "ph": 7.1,
            "do": 4.5,
            "temperature": 28.2,
            "turbidity": 25,
            "waste_detection": None
        }
    },
    {
        "id": "st-3",
        "name": "Khlong Lat Phrao",
        "lat": 13.8136,
        "lng": 100.5847,
        "source": "Unknown",
        "timestamp": None,
        "data": None # Simulating "No data available"
    }
]

MOCK_HISTORY = {
    "st-1": [
        {"time": "08:00", "ph": 7.0, "do": 3.5},
        {"time": "10:00", "ph": 6.9, "do": 3.4},
        {"time": "12:00", "ph": 6.9, "do": 3.3},
        {"time": "14:00", "ph": 6.8, "do": 3.2},
    ],
    "st-2": [
        {"time": "08:00", "ph": 7.2, "do": 4.8},
        {"time": "10:00", "ph": 7.2, "do": 4.7},
        {"time": "12:00", "ph": 7.1, "do": 4.6},
        {"time": "14:00", "ph": 7.1, "do": 4.5},
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thailand-data.js')
def thailand_data():
    return send_from_directory('.', 'thailand-data.js')

@app.route('/thailand.geojson')
def thailand_geojson():
    return send_from_directory('.', 'thailand.geojson')

@app.route('/creator.jpg')
def creator_img():
    return send_from_directory('.', 'creator.jpg')

@app.route('/api/stations')
def get_stations():
    return jsonify(MOCK_STATIONS)

@app.route('/api/history/<station_id>')
def get_history(station_id):
    if station_id in MOCK_HISTORY:
        return jsonify(MOCK_HISTORY[station_id])
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
