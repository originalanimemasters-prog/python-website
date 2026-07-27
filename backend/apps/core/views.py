from django.db import connection
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_status = "connected"
            status = "healthy"
        except Exception:
            db_status = "disconnected"
            status = "unhealthy"

        return Response(
            {
                "status": status,
                "database": db_status,
                "version": "1.0.0",
                "timestamp": timezone.now().isoformat(),
            }
        )