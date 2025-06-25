import unittest

import pytest

from bookings.exceptions import MissingPMSBookingField
from bookings.mapper import Mapper


class TestMapping(unittest.TestCase):

    def test_booking_mapping(self):

        # happy path
        raw = {
            'id': '123',
            'guest_name': 'Alice Smith',
            'room': '201',
            'from_date': '2025-07-01',
            'to_date': '2025-07-05',
        }
        expected = {
            'booking_id': '123',
            'guest': 'Alice Smith',
            'room_number': '201',
            'check_in_date': '2025-07-01',
            'check_out_date': '2025-07-05',
            'misc': {}
        }
        self.assertEqual(Mapper.map_pms_booking(raw), expected)

        # misc fields been collected
        raw = {
            'id': '123',
            'guest_name': 'Alice Smith',
            'room': '201',
            'from_date': '2025-07-01',
            'to_date': '2025-07-05',
            'payment': 'declined'
        }
        expected = {
            'booking_id': '123',
            'guest': 'Alice Smith',
            'room_number': '201',
            'check_in_date': '2025-07-01',
            'check_out_date': '2025-07-05',
            'misc': {'payment': 'declined'}
        }
        self.assertEqual(Mapper.map_pms_booking(raw), expected)

        # validate the missing fields
        raw = {
            'id': '123',
            'guest_name': 'Alice Smith',
            'from_date': '2025-07-01',
            'to_date': '2025-07-05',
            'payment': 'declined'
        }
        expected = {
            'booking_id': '123',
            'guest': 'Alice Smith',
            'room_number': '201',
            'check_in_date': '2025-07-01',
            'check_out_date': '2025-07-05',
            'misc': {'payment': 'declined'}
        }
        with pytest.raises(MissingPMSBookingField):
            self.assertEqual(Mapper.map_pms_booking(raw), expected)
