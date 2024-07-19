
import requests

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"start_date": "2013-01-01",
	"end_date": "2023-01-01",
	"hourly": "temperature_2m"
}
response = requests.get(url, params=params)

data = response.json()["hourly"]["temperature_2m"]

cold_hours=0
for n in data:
	if n < 7.00:
		cold_hours +=1

mean_in_a_year= cold_hours/10
print(mean_in_a_year)