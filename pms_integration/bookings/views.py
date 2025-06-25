import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import Services
from .mapper import Mapper
from .exceptions import PMSAPIError


class PMSBookingsView(APIView):
    """
    View to fetch the transformed PMS booking info
    """

    def get(self, request):
        """
        transform the PMS booking data into internal format
        :param request:
        :return:
        """
        try:
            raw_data = Services.fetch_pms_bookings()
            transformed_data = Mapper.map_pms_bookings(raw_data)

            return Response(transformed_data, status=status.HTTP_200_OK)
        except PMSAPIError as e:
            logging.exception(f'failed to fetch the mocked data. {str(e)}')

            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
