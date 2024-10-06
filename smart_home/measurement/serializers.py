from measurement.models import Measurement, Sensor
from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    Measurement = MeasurementSerializer(read_only=True, many=True)
   
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'Measurement']

