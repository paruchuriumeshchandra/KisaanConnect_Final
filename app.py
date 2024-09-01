from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = 'cb6aef422a4b88ba42a6b27a745072da'  # Replace with your OpenWeatherMap API key
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather',
                                params={'q': city, 'appid': api_key, 'units': 'metric'})
        weather_data = response.json()
    return render_template('index.html', weather_data=weather_data)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/market-updates')
def market_updates():
    return render_template('market_updates.html')

@app.route('/pests-prediction')
def pests_prediction():
    return render_template('pests_prediction.html')

@app.route('/disease-prediction')
def disease_prediction():
    return render_template('disease_prediction.html')

@app.route('/virtual-farmer-assistant')
def virtual_farmer_assistant():
    return render_template('virtual_farmer_assistant.html')

@app.route('/government-schemes')
def government_schemes():
    return render_template('government_schemes.html')

@app.route('/knowledge-sharing-forum')
def knowledge_sharing_forum():
    return render_template('knowledge_sharing_forum.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/cropSpecAdvice')
def cropSpecAdvice():
    return render_template('cropSpecAdvice.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you can add your logic to validate the user's login credentials
        # If login is successful, redirect to the dashboard
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
