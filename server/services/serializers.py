from rest_framework import serializers

from .models import Home, Room, Specs


class SpecsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Specs
		fields = '__all__'


