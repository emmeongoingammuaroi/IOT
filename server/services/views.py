from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from .mqtt import *
from .models import Home, Room, Specs
from .serializers import SpecsSerializer


class SpecsView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		data = {}
		spec = Specs.objects.first()
		data = {
		    "room": spec.room.title,
		    "temperature": spec.temperature,
		    "gas": spec.gas,
		    "status": spec.status,
		    "humidity": spec.humidity,
		}
		return Response(data, status=status.HTTP_200_OK)


class PublishView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		pub_message = json.dumps(request.data)
		client.publish(MQTT_PUB_TOPIC, pub_message)
		data = {
		    'message': 'Publish Successfully'
		}
		return Response(data, status=status.HTTP_200_OK)
