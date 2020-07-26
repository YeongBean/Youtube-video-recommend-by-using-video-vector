from rest_framework import serializers
from api.models import Video, VideoFile


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


class VideoFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoFile
        fields = '__all__'
