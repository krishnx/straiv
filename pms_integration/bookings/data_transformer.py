import logging

from bookings.mapper import Mapper
from bookings.models import Booking
from bookings.serlalizers import BookingSerializer
from bookings.services import Services

logger = logging.getLogger(__name__)


class DataTransformer:

    def __init__(self):
        self.services = Services()
        self.mapper = Mapper()

    def transform(self, save=False):
        raw_data = self.services.fetch_pms_bookings()
        transformed_data = self.mapper.map_pms_bookings(raw_data)

        if save:
            logger.debug('saving booking data in db')
            for booking in transformed_data:
                Booking.objects.update_or_create(
                    booking_id=booking['booking_id'],
                    defaults={
                        'guest': booking['guest'],
                        'room_number': booking['room_number'],
                        'check_in_date': booking['check_in_date'],
                        'check_out_date': booking['check_out_date'],
                        'misc': booking.get('misc', {})
                    }
                )

        serializer = BookingSerializer(transformed_data, many=True)

        return serializer.data
