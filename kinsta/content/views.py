from django.shortcuts import render
from rest_framework.views import APIView

from .models import Feed
# Create your views here.

class test(APIView):
    def get(self, request):
        return render(request, 'content/test.html') # html 파일 위치
    
class main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all() # select * from content_feed
        
        for f in feed_list:
            print(f.content)
        
        return render(request, 'kinsta/main.html', context=dict(feed_list=feed_list))