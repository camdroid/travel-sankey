import requests
import json
from secrets import qpx_api_key
from flight_finder import FlightFinder


class QPXFlightFinder(FlightFinder):
    def get_one_way_flight_details(self, orig, dest, outbound_date,
                                   inbound_date):
        params = {
          "request": {
            "slice": [
              {
                "origin": orig,
                "destination": dest,
                "date": outbound_date
              }
            ],
            "passengers": {
              "adultCount": 1
            },
            "solutions": 500,
            "refundable": False
          }
        }

        response = requests.post(url, data=json.dumps(params),
                                 headers=self.headers)
        data = response.json()


if __name__ == '__main__':
    url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" \
        + qpx_api_key
    ff = QPXFlightFinder(url)
    ff.get_one_way_flight_details('DTW', 'SFO', '2016-11-01', '2016-11-04')
