from django.urls import path, include
from django.conf.urls import url
from api.views import VideoFileUploadView, VideoFileList, FileListView
from . import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

router = DefaultRouter()
router.register('db/videofile', views.VideoFileViewSet)
router.register('db/video', views.VideoViewSet)

urlpatterns = [
    # FBV
    path('api/upload', VideoFileUploadView.as_view(), name="file-upload"),
    path('api/upload/<int:pk>/', VideoFileList.as_view(), name="file-list"),
    path('api/file', FileListView.as_view(), name="file"),
    url(r'^(?P<path>.*)$', TemplateView.as_view(template_name='index.html')),
    # path('api/upload', views.VideoFile_Upload),
    path('', include(router.urls)),
]
