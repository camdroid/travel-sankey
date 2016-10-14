import json
import requests
from secrets import qpx_api_key

url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + qpx_api_key
headers = {'content-type': 'application/json'}

params = {
  "request": {
    "slice": [
      {
        "origin": "DTW",
        "destination": "LIM",
        "date": "2017-01-19"
      }
    ],
    "passengers": {
      "adultCount": 1
    },
    "solutions": 500,
    "refundable": False
  }
}

response = requests.post(url, data=json.dumps(params), headers=headers)
data = response.json()
# print(data)
data['trips']['data'].pop('aircraft')
data['trips']['data'].pop('airport')
data['trips']['data'].pop('carrier')
data['trips']['data'].pop('city')
data['trips']['data'].pop('tax')

trips = []

for option in data['trips']['tripOption']:
    option.pop('pricing')
    for flight_slice in option['slice']:
        for segment in flight_slice['segment']:
            for leg in segment['leg']:
                trip = {'arrival': leg['arrivalTime'],
                        'departure': leg['departureTime'],
                        'destination': leg['destination'],
                        'origin': leg['origin']}
                trips.append(trip)

import pdb; pdb.set_trace()
pass
