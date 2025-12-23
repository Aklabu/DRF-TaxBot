from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status

class CustomResponse:
    @staticmethod
    def success(message, data=None, status_code=200):
        response_data = {
            "success": True,
            "statusCode": status_code,
            "message": message,
            "timestamp": timezone.now().isoformat(),
            "data": data,
            "errors": None
        }
        
        return Response(response_data, status=status_code)
