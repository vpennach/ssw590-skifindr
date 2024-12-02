from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from geopy.geocoders import Nominatim

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to geocode a location using geopy
def geocode_location(location):
    geolocator = Nominatim(user_agent="ssw590-skifindr-app")
    try:
        location_data = geolocator.geocode(location)
        if location_data:
            return {
                "latitude": location_data.latitude,
                "longitude": location_data.longitude
            }
    except Exception as e:
        print(f"Error: {e}")
    return None

# API endpoint to get coordinates
@app.route('/api/geocode', methods=['POST'])
def geocode():
    data = request.json
    location = data.get('location')
    if not location:
        return jsonify({'error': 'Location is required'}), 400

    coords = geocode_location(location)
    if coords:
        return jsonify(coords)
    else:
        return jsonify({'error': 'Unable to geocode location'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
