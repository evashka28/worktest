from django.contrib.auth.hashers import make_password

from .models import CustomUser, Room, Reservation
from rest_framework.serializers import ModelSerializer


class CustomUserSerializer(ModelSerializer):
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = CustomUser
        fields = 'all'


#TODO
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = 'all'


class ReservationSerializer(ModelSerializer):
    def is_valid(self, *, raise_exception=False):
        if not super().is_valid():
            return False
        date_from = self.data.get('date_from')
        date_to = self.data.get('date_to')
        return self.Meta.model.objects.all().filter(date_from__lt=date_from)

    class Meta:
        model = Reservation
        fields = 'all'