from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Serve the front-end HTML file
@app.route('/')
def index():
    return send_from_directory('/Users/aleenasultan/Documents/GitHub/khanhcao2027.github.io','personal_details.html')

@app.route('/calculateTax', methods=['POST'])

def calculate_tax():
    data = request.json
    age = data['age']
    nationality = data['nationality']
    work_status = data['workStatus']
    dependency = data['dependency']

    # Step-by-step guide logic
    if nationality == 'domestic':
        print("Domestic student")
        if dependency == 'yes':
            guide = "Since you're a tax-dependent domestic student, you may need to file..."
        else:
            guide = "As a non-dependent domestic student, you will need to..."
    else:  # international
        if work_status == 'yes':
            guide = "Since you're an international student who worked, you'll need 3 forms..."
        else:
            guide = "As an international student who didn't work, you'll need 2 forms..."

    return jsonify({'guide': guide})

if __name__ == '__main__':
    app.run(debug=True)