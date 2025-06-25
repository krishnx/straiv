from bookings.exceptions import InvalidPMSBookingData, MissingPMSBookingField


class Mapper:
    MANDATORY_INTERNAL_FIELDS = ['booking_id', 'guest', 'room_number', 'check_in_date', 'check_out_date']
    MANDATORY_PMS_BOOKING_FIELDS = ['id', 'guest_name', 'room', 'from_date', 'to_date']

    @classmethod
    def _validate_pms_booking(cls, pms_booking):
        if not pms_booking:
            raise InvalidPMSBookingData('undefined PMS booking')

        for field in cls.MANDATORY_PMS_BOOKING_FIELDS:
            if field in pms_booking:
                continue

            raise MissingPMSBookingField(f'missing field from the PMS Booking data: {field}')

    @classmethod
    def map_pms_booking(cls, pms_booking):
        cls._validate_pms_booking(pms_booking)

        transformed_data = {
            'booking_id': pms_booking['id'],
            'guest': pms_booking['guest_name'],
            'room_number': pms_booking['room'],
            'check_in_date': pms_booking['from_date'],
            'check_out_date': pms_booking['to_date'],
            'misc': {}
        }

        # if the pms_booking data has more fields, lets not loose them
        for field in pms_booking:
            if field in cls.MANDATORY_PMS_BOOKING_FIELDS:
                continue

            transformed_data['misc'][field] = pms_booking[field]

        return transformed_data

    @classmethod
    def map_pms_bookings(cls, pms_data):
        if not pms_data:
            raise ValueError('undefined pms data')

        return [cls.map_pms_booking(data) for data in pms_data]
