from rest_framework.views import APIView
from rest_framework.response import Response

class PublicBookingView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response({"message": "API pública OK"})
