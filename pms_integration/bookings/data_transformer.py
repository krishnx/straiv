import logging

from bookings.mapper import Mapper
from bookings.serlalizers import BookingSerializer
from bookings.services import Services

logger = logging.getLogger(__name__)


class DataTransformer:

    def __init__(self):
        self.services = Services()
        self.mapper = Mapper()

    def map_data(self, raw_data):
        if not raw_data:
            raise ValueError('undefined raw data')

        if not isinstance(raw_data, list):
            raw_data = [raw_data]

        return self.mapper.map_pms_bookings(raw_data)

    def transform(self, raw_data=None):
        """
        Either transform the input raw data or fetch it from the source

        :param raw_data:
        :return: transformed data
        """
        if not raw_data:
            raw_data = self.services.fetch_pms_bookings(mock=True)

        transformed_data = self.mapper.map_pms_bookings(raw_data)
        serializer = BookingSerializer(transformed_data, many=True)

        return serializer.data
