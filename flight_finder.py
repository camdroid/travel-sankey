

class FlightFinder(object):
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'content-type': 'application/json'}

    def get_roundtrip_flight_details(self, orig, dest, outbound_date,
                                     inbound_date):
        raise Exception('Method not implemented')
