from django.shortcuts import render
from rest_framework.views import APIView

from .models import Feed
# Create your views here.

class test(APIView):
    def get(self, request):
        return render(request, 'content/test.html') # html 파일 위치
    
class main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed
        
        for f in feed_list:
            print(f.content)
        
        # 사전 형식으로 전달 { key(템플릿으로 전달할 이름) : value }
        return render(request, 'kinsta/main.html', context=dict(feeds=feed_list))