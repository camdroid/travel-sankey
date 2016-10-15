import json
import requests
from secrets import skyscanner_key_2 as skyscanner_key


class FlightFinder(object):
    # base_url = 'https://partners.api.skyscanner.net/apiservices/'
    base_url = 'https://api.skyscanner.net/apiservices/'
    endpoint = 'browsequotes/v1.0/'
    stuff = 'US/USD/en-US/'
    headers = {'content-type': 'application/json'}

    def get_roundtrip_flight_details(self, orig, dest, outbound_date,
                                     inbound_date=None):
        query = '{}/{}/{}'.format(orig, dest, outbound_date)
        if inbound_date is not None:
            query = '{}/{}'.format(query, inbound_date)
        url = '{}{}{}'.format(self.base_url, self.endpoint, query)
        return self.get_request(url)

    def get_request(self, url, params=None):
        if params is None:
            params = json.dumps({})
        url = '{}?apiKey={}'.format(url, skyscanner_key)
        import pdb; pdb.set_trace()
        response = requests.get(url, data=params, headers=self.headers)
        data = response.json()
        return data


if __name__ == '__main__':
    ff = FlightFinder()
    data = ff.get_roundtrip_flight_details('DTW', 'SFO', '2016-11')
    quotes = data['Quotes']

    prices = [quote['MinPrice'] for quote in quotes]
    print('Minimum Price: ${}'.format(min(prices)))
    print([quote for quote in quotes if quote['MinPrice'] == min(prices)])
