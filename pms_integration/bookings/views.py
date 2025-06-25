import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .data_transformer import DataTransformer
from .exceptions import PMSAPIError

logger = logging.getLogger(__name__)


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
            transformed_data = DataTransformer().transform(request.GET.get('save'))

            return Response(transformed_data, status=status.HTTP_200_OK)
        except PMSAPIError as e:
            logger.exception(f'failed to fetch the mocked data. {str(e)}')

            return Response({'error': str(e)}, status=status.HTTP_502_BAD_GATEWAY)
