from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Feed

from uuid import uuid4
import os
from kinsta.settings import MEDIA_ROOT

from user.models import user

# Create your views here.
class test(APIView):
    def get(self, request):
        return render(request, 'content/test.html') # html 파일 위치

class main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed
                
        #
        try:
            user_email = request.session['email']
        except KeyError:
            print("세션 비어있음")
            return render(request, 'user/login.html')              
        
        login_user = user.objects.filter(user_email = user_email).first() # 유저 정보
        print("유저 이름 :", login_user.user_name)
        print("유저 이메일 :", login_user.user_email)
        print("유저 닉네임 :", login_user.user_nickname)
        #
        
        # 사전 형식으로 전달 { key(템플릿으로 전달할 이름) : value }
        return render(request, 'kinsta/main.html', context=dict(feeds=feed_list, user = login_user))

# from uuid import uuid4
# import os
# from kinsta.settings import MEDIA_ROOT

class upload_feed(APIView):
    def post(self, request):
        # file = request.data.get('file')
        
        file = request.FILES['file']
        
        # 파일 이름을 고유한 id로 변경 (프로그램에서 다루기 쉽게)
        uuid_name = uuid4().hex
        # /MEDIA_ROOT/uuid_name로 이미지 저장
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        
        # 파일 읽기
        with open(save_path, 'wb+') as destination:
            for chunk  in file.chunks():
                destination.write(chunk)
        
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_img = request.data.get('profile_img')
        
        img_location = uuid_name
        
        print(file)
        print(uuid_name)
        print(content)
        print(user_id)
        print(profile_img)
        
        Feed.objects.create(profile_image = profile_img, user_id = user_id,
                            image = img_location,content = content,
                            like_count = 0)

        return Response(status=200)