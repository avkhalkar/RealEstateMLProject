import warnings
warnings.filterwarnings("ignore")


from flask import Flask, request, jsonify
import util

# Creates instance of the Flask app. 
# The __name__ argument tells Flask where the app is located, 
# so it can correctly find templates, static files, and set up paths.
app = Flask(__name__)


# methods=['GET']: Implies that route only responds to
# GET requests (used to fetch data, not modify it).
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# methods=['GET']: Implies that route only responds to GET and POSTrequests 
# (used to fetch data, and modify it).

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    
    # This retrieves data sent in the form body of a POST request.
    
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    # Sent output can be accessed by any origin
    response.headers.add('Access-Control-Allow-Origin', '*')  

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()