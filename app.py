import requests
from flask import Flask, render_template, request , redirect

app = Flask(__name__)


API_KEY = "415f4a8328734b7d951502ad9a131c69"

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city_name = request.form.get('city').title()
    else:
        city_name = "Pune"
        
        
    url = f"https://api.weatherbit.io/v2.0/current?&city={city_name}&country=IN&key={API_KEY}&include=minutely"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)  # full JSON response

        weather = {
            'city': city_name,
            'temp': data['data'][0]['temp'],
            'description': data['data'][0]['weather']['description'],
            'wind_spd':data['data'][0]['wind_spd'],
            'feel_like': data['data'][0]['app_temp'],
            'humidity': data['data'][0]['rh'],
            'icon_code': data['data'][0]['weather']['icon']
        }
        
        
       
    else:
        print("Error:", response.status_code)
    

    return render_template('index.html', weather=weather)


if __name__ == '__main__':
    app.run(debug=True)