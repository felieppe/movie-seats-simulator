import requests, json

class API:
    # Constructor
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    # Method to make a request 
    def make_request(self, method, url, data=None):
        response = requests.request(method, url, headers=self.headers, data=json.dumps(data) if data else None)
        return response.json()

    # Getter methods
    def get_base_url(self):
        return self.base_url
    def get_headers(self):
        return self.headers

    # Setter methods
    def set_base_url(self, base_url):
        self.base_url = base_url
    def set_headers(self, headers):
        self.headers = headers

    # :GET Methods
    def get_status_of_all_seats(self):
        url = f"{self.base_url}/seats"
        return self.make_request("GET", url)

    def get_status_of_available_seats(self):
        url = f"{self.base_url}/seats/available"
        return self.make_request("GET", url)

    def get_status_of_booked_seats(self):
        url = f"{self.base_url}/seats/booked"
        return self.make_request("GET", url)

    def get_status_of_reserved_seats(self):
        url = f"{self.base_url}/seats/reserved"
        return self.make_request("GET", url)

    def get_status_of_seat_by_id(self, id):
        url = f"{self.base_url}/seats/{id}"
        return self.make_request("GET", url)

    # :POST Methods
    def book_seat_by_id(self, id, data):
        url=f"{self.base_url}/seats/book/{id}"
        return self.make_request("POST", url, data)

    def reserve_seat_by_id(self, id, data):
        url=f"{self.base_url}/seats/reserve/{id}"
        return self.make_request("POST", url, data)

    # :DELETE Methods
    def release_seat_by_id(self, id, data):
        url=f"{self.base_url}/seats/release/{id}"
        return self.make_request("DELETE", url, data)