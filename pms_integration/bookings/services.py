import requests
from .exceptions import PMSAPIError


class Services:
    PMS_API_URL = 'https://mocked-pms.straiv.com/api/bookings'
    MOCKED_DATA = [
        {
            'id': '123',
            'guest_name': 'Foo Bar',
            'room': '101',
            'requested_facilities': ['pool', 'king sized bed'],
            'payment': 'prepaid',
            'from_date': '2025-06-20',
            'to_date': '2025-06-25'
        },
    ]

    @classmethod
    def fetch_pms_bookings(cls):
        try:
            # response = requests.get(cls.PMS_API_URL, timeout=5)
            # response.raise_for_status()
            # return response.json()
            return cls.MOCKED_DATA
        except requests.RequestException as e:
            raise PMSAPIError(f'Failed to fetch data from PMS: {str(e)}')
