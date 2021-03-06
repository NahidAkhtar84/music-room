from django.shortcuts import render
from rest_framework import generics, status
from .models import Room
from .serializers import RoomSerializers, CreateRoomSerializser
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class RoomCreateView(APIView):
    serializer_class = CreateRoomSerializser

    def post(self, request, *args):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get("guest_can_pause")
            votes_to_skip = serializer.data.get("votes_to_skip")
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
                room.save()

            return Response(RoomSerializers(room).data, status=status.HTTP_201_CREATED)

