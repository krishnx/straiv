import unittest
from bookings.mapper import Mapper

class TestMapping(unittest.TestCase):
    def test_booking_mapping(self):
        raw = {
            "id": "123",
            "guest_name": "Alice Smith",
            "room": "201",
            "check_in": "2025-07-01",
            "check_out": "2025-07-05"
        }
        expected = {
            "booking_id": "123",
            "guest": "Alice Smith",
            "room_number": "201",
            "check_in_date": "2025-07-01",
            "check_out_date": "2025-07-05"
        }
        self.assertEqual(Mapper.map_pms_booking(raw), expected)