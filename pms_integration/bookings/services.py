import logging

import requests
from .exceptions import PMSAPIError

logger = logging.getLogger(__name__)

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
            response = requests.get(cls.PMS_API_URL, timeout=5)
            response.raise_for_status()
            # return cls.MOCKED_DATA

            logger.debug(f'fetched data from {cls.PMS_API_URL}')

            return response.json()
        except requests.RequestException as e:

            raise PMSAPIError(f'Failed to fetch data from PMS: {str(e)}')
