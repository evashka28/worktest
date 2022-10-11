from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from Booking.models import CustomUser, Room, Reservation
from Booking.permissions import IsAdminUserOrReadOnly
from Booking.serializers import CustomUserSerializer, RoomSerializer, ReservationSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserTokenViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAdminUser, ]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['reservations']


#TODO
class SignUpViewSet(CreateAPIView):
    model = CustomUser
    permission_classes = [AllowAny, ]
    serializer_class = CustomUserSerializer

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = Response(data={'status': 'created'}, status=status.HTTP_201_CREATED)
        return response


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = [IsAdminUserOrReadOnly, ]
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'number_of_guests', 'reservation__date_from']


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    # permission_classes = [IsAuthenticated, ]
    serializer_class = ReservationSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return Reservation.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)