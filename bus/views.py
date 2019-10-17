from django.conf import settings
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from bus.models import FromTo

from bus.serializers import FromToSerializer
from datetime import datetime

# Create your views here.

class FromToList(generics.ListCreateAPIView):
    queryset = FromTo.objects.all()
    serializer_class = FromToSerializer

    def list(self, request):
        self.serializer_class = FromToSerializer
        return super(FromToList, self).list(request)

class FromToDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FromTo.objects.all()
    serializer_class = FromToSerializer

    def retrieve(self, request, pk):
        queryset = self.get_object()
        serializer = FromToSerializer(queryset, many=False)
        return Response(serializer.data)

