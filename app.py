from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import random

app = Flask(__name__, static_folder='static')
CORS(app)

# -------------------- Clinic Data --------------------
clinic_data = {
    "alkapuri": {
        "1": {"name": "Shraddha Clinic", "doctor": "Dr.Misthi", "address": "Alkapuri, Vadodara", "contact": "+91 98765 43210"},
        "2": {"name": "Shree Clinic", "doctor": "Dr.Aadarsh", "address": "Alkapuri, Vadodara", "contact": "+91 87654 32109"},
        "3": {"name": "Patel Clinic", "doctor": "Dr.Divyang Rathva", "address": "Alkapuri, Vadodara", "contact": "+91 76543 21098"}
    },
    "andheri": {
        "1": {"name": "CareWell Clinic", "doctor": "Dr.Sneha", "address": "Andheri, Mumbai", "contact": "+91 99887 66554"},
        "2": {"name": "Pulse Clinic", "doctor": "Dr.Rajeev", "address": "Andheri, Mumbai", "contact": "+91 88776 55443"}
    },
    "ernakulam": {
        "1": {"name": "Lotus Clinic", "doctor": "Dr.Anu", "address": "Ernakulam, Kochi", "contact": "+91 77665 44332"}
    }
}

# -------------------- Illness Data --------------------
illness_data = {
    "gujarat": {
        "vadodara": {
            "cancer": ['Sterling Hospital', 'HCG Cancer Center', 'Shalby Hospital'],
            "heart": ['Baroda Heart Institute', 'Bankers Heart Hospital'],
            "kidney": ['Kidney Care Hospital', 'Apollo Hospital'],
            "surgical": ['Gujarat Surgical Hospital', 'Pinaksh Hospital']
        },
        "ahmedabad": {
            "cancer": ['GCRI', 'Apollo Ahmedabad'],
            "heart": ['CIMS Hospital', 'Zydus Hospital'],
            "kidney": ['IKDRC', 'Sal Hospital']
        }
    },
    "maharashtra": {
        "mumbai": {
            "cancer": ['Tata Memorial Hospital', 'Kokilaben Dhirubhai Ambani Hospital'],
            "heart": ['Asian Heart Institute', 'Nanavati Hospital'],
            "kidney": ['Bombay Hospital', 'Lilavati Hospital']
        },
        "pune": {
            "cancer": ['Ruby Hall Clinic', 'Sahyadri Hospital'],
            "heart": ['Jehangir Hospital', 'Columbia Asia'],
            "kidney": ['Noble Hospital', 'Deenanath Mangeshkar Hospital']
        }
    },
    "kerala": {
        "kochi": {
            "cancer": ['Amrita Institute', 'Aster Medcity'],
            "heart": ['Lakeshore Hospital', 'Renai Medicity'],
            "kidney": ['KIMS Hospital', 'Medical Trust Hospital']
        }
    }
}

# -------------------- Routes --------------------
@app.route('/api/clinic/<area>', methods=['POST'])
def get_clinic(area):
    choice = request.json.get('choice')
    area_info = clinic_data.get(area.lower())
    if area_info:
        return jsonify(area_info.get(choice, {"error": "Invalid clinic choice"}))
    return jsonify({"error": "Invalid area"})

@app.route('/api/illness/<state>/<city>', methods=['POST'])
def get_hospital(state, city):
    illness = request.json.get('illness')
    state_info = illness_data.get(state.lower())
    if state_info:
        city_info = state_info.get(city.lower())
        if city_info:
            hospital_list = city_info.get(illness.lower())
            if hospital_list:
                return jsonify({"recommended_hospital": random.choice(hospital_list)})
    return jsonify({"error": "Invalid illness or location"})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
