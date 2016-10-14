import json
import requests
from secrets import skyscanner_key

base_url = 'http://partners.api.skyscanner.net/apiservices/'
endpoint = 'browsequotes/v1.0/'
stuff = 'US/USD/en-US/'
airports = '{origin}/{dest}'.format(origin='DTW', dest='SFO')
# dates = '{start_date}/{end_date}'.format(start_date='2016-10-17',
                                        #  end_date='2016-10-24')
dates = '{start_date}'.format(start_date='2016-11')
url = '{base}{endpoint}{stuff}{airports}/{dates}?apiKey={key}'.format(
    base=base_url, endpoint=endpoint, stuff=stuff, airports=airports,
    dates=dates, key=skyscanner_key
)
headers = {'content-type': 'application/json'}

response = requests.get(url, data=json.dumps({}), headers=headers)
data = response.json()
# print(data)
quotes = data['Quotes']

prices = [quote['MinPrice'] for quote in quotes]
print('Minimum Price: ${}'.format(min(prices)))
print([quote for quote in quotes if quote['MinPrice'] == min(prices)])

import pdb; pdb.set_trace()
pass
