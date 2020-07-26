from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import viewsets
import os
from django.http.request import QueryDict
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from api.models import Video, VideoFile
from api.serializers import VideoSerializer, VideoFileSerializer
from api import file_upload_path 

import subprocess
import shlex
import json
# Create your views here.
import sys
sys.path.insert(0, "/home/jun/documents/univ/PKH_Project1/web/backend/yt8m/esot3ria")
import inference_pb

def with_ffprobe(filename):

    result = subprocess.check_output(
            f'ffprobe -v quiet -show_streams -select_streams v:0 -of json "{filename}"',
            shell=True).decode()
    fields = json.loads(result)['streams'][0]
    duration = int(float(fields['duration']))
    return duration

def index(request):
    return render(request, template_name='index.html')

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoFileViewSet(viewsets.ModelViewSet):
    queryset = VideoFile.objects.all()
    serializer_class = VideoFileSerializer


class VideoFileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        videoFiles = VideoFile.objects.all()
        serializer = VideoFileSerializer(videoFiles, many=True)
        return Response(serializer.data)

    def post(self, req, *args, **kwargs):
        # 동영상 길이
        runTime = 0
       # 요청된 데이터를 꺼냄( QueryDict)         
        new_data = req.data.dict()
        
        # 요청된 파일 객체
        file_name = req.data['file']
        threshold = req.data['threshold']
        
        # 저장될 파일의 풀path를 생성        
        new_file_full_name = file_upload_path(file_name.name)
        # 새롭게 생성된 파일의 경로
        file_path = '-'.join(new_file_full_name.split('-')[0:-1])        

        new_data['file_path'] = file_path
        new_data['file_origin_name'] = req.data['file'].name
        new_data['file_save_name'] = req.data['file']

        new_query_dict = QueryDict('', mutable=True)
        new_query_dict.update(new_data)
        file_serializer = VideoFileSerializer(data = new_query_dict)
        
        if file_serializer.is_valid():
            file_serializer.save()     
            # 동영상 길이 출력  
            runTime = with_ffprobe('/'+file_serializer.data['file_save_name'])
            print(runTime)
            print(threshold)
            process = subprocess.Popen(['./runMediaPipe.sh %s %s' %(file_serializer.data['file_save_name'],runTime,)], shell = True)
            process.wait()


            result =  inference_pb.inference_pb('/tmp/mediapipe/features.pb', threshold)

            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class VideoFileList(APIView):

    def get_object(self, pk):
        try:
            return VideoFile.objects.get(pk=pk)
        except VideoFile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoFileSerializer(video)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoFileSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FileListView(APIView):
    def get(self, request):
        data = {
            "search": '',
            "limit": 10,
            "skip": 0,
            "order": "time",
            "fileList": [
                {
                    "name": "1.png",
                    "created": "2020-04-30",
                    "size": 10234,
                    "isFolder": False,
                    "deletedDate": "",
                },
                {
                    "name": "2.png",
                    "created": "2020-04-30",
                    "size": 3145,
                    "isFolder": False,
                    "deletedDate": "",
                },
                {
                    "name": "3.png",
                    "created": "2020-05-01",
                    "size": 5653,
                    "isFolder": False,
                    "deletedDate": "",
                },
            ]
        }
        return Response(data)
    def post(self, request, format=None):
        data = {
            "isSuccess": True,
            "File": {
                "name": "test.jpg",
                "created": "2020-05-02",
                "deletedDate": "",
                "size": 2312,
                "isFolder": False
            }
        }
        return Response(data)