import logging

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .data_transformer import DataTransformer
from .exceptions import PMSAPIError
from .models import Booking
from .serlalizers import BookingSerializer

logger = logging.getLogger(__name__)


class PMSBookingsView(APIView):
    """
    View to fetch the transformed PMS booking info
    """

    def get(self, request):
        """
        GET /api/integrations/pms/bookings/
        transform the PMS booking data into internal format
        :param request:
        :return:
        """
        try:
            transformed_data = DataTransformer().transform()

            return Response(transformed_data, status=status.HTTP_200_OK)
        except PMSAPIError as e:
            logger.exception(f'failed to fetch the mocked data. {str(e)}')

            return Response({'error': str(e)}, status=status.HTTP_502_BAD_GATEWAY)


class BookingCreateView(APIView):
    """
    POST /api/integrations/pms/bookings/save/
    Save booking data into the system.
    """

    @swagger_auto_schema(
        request_body=BookingSerializer,
        responses={
            201: openapi.Response(description="Booking created/updated successfully"),
            400: "Invalid booking data"
        }
    )
    def post(self, request):
        transformed_data = DataTransformer().map_data(request.data)
        serializer = BookingSerializer(data=transformed_data[0])

        if not serializer.is_valid():
            logger.error(f'Invalid booking data: {serializer.errors}')

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        booking, created = Booking.objects.update_or_create(
            booking_id=serializer.validated_data['booking_id'],
            defaults=serializer.validated_data
        )

        return Response({'message': 'Booking saved', 'created': created}, status=status.HTTP_201_CREATED)
