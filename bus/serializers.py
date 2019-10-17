from rest_framework.serializers import ModelSerializer
from bus.models import FromTo

class FromToSerializer(ModelSerializer):

    class Meta:
        model = FromTo
        fields = (
            'id',
            'get_from_lat',
            'get_from_long',
            'get_to_lat',
            'get_to_long',
        )
        read_only_fields = fields