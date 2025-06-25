import logging

import requests
from .exceptions import PMSAPIError
from .models import Booking
from typing import List, Dict

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
    def fetch_pms_bookings(cls, mock=False):
        try:
            if mock:
                return cls.MOCKED_DATA

            response = requests.get(cls.PMS_API_URL, timeout=5)
            response.raise_for_status()

            logger.debug(f'fetched data from {cls.PMS_API_URL}')

            return response.json()
        except requests.RequestException as e:

            raise PMSAPIError(f'Failed to fetch data from PMS: {str(e)}')

    @classmethod
    def save_bookings(cls, mapped_bookings: List[Dict]):
        """
        Saves or updates mapped booking records into the Booking model.
        :param mapped_bookings: List of dicts in internal booking format
        """
        if not mapped_bookings:
            logger.debug('no booking data to save')

            return None

        for booking in mapped_bookings:
            Booking.objects.update_or_create(
                booking_id=booking['booking_id'],
                defaults={
                    'guest': booking['guest'],
                    'room_number': booking['room_number'],
                    'check_in_date': booking['check_in_date'],
                    'check_out_date': booking['check_out_date'],
                    'misc': booking.get('misc', {}),
                }
            )
