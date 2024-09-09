from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from user.models import user

from uuid import uuid4
import os
from kinsta.settings import MEDIA_ROOT



# Create your views here.
class test(APIView):
    def get(self, request):
        return render(request, "content/test.html")  # html 파일 위치


class main(APIView):
    def get(self, request):
        print("main 접속")
        
        #
        try:
            login_email = request.session["email"]
        except KeyError:
            print("세션 비어있음")
            return render(request, "user/login.html")

        login_user = user.objects.filter(user_email=login_email).first()  # 유저 정보
        print("유저 닉네임 :", login_user.user_nickname)
        #
        
        feed_object_list = Feed.objects.all().order_by("-id")  # select * from content_feed
        feed_list = []
        
        for feed in feed_object_list:
            upload_user = user.objects.filter(user_email = feed.user_email).first()
            # print("피드 아이디 :", feed.id)
            
            # 댓글들이 담겨있는 리스트
            comment_object_list = comment.objects.filter(feed_id = feed.id)
            comment_list = []
            
            for each_comment in comment_object_list:
                comment_user = user.objects.filter(user_email = each_comment.email).first()
                comment_list.append(dict(
                    nickname = each_comment.nickname,
                    content = each_comment.comment_content,
                    profile_img = comment_user.profile_img
                ))
            #
                        
            like_object = like.objects.filter(feed_id = feed.id, is_like = True)
            like_count = like_object.count()
            
            is_liked = like.objects.filter(feed_id = feed.id, email = login_email, is_like = True).exists()
            
            is_bookmarked = bookmark.objects.filter(feed_id = feed.id, email = login_email, is_bookmark = True).exists()
            
            feed_list.append(dict(
                image = feed.image,
                content = feed.content,
                nickname = upload_user.user_nickname,
                profile_img = upload_user.profile_img,
                feed_id = feed.id,
                comment_list = comment_list,
                like_count = like_count,
                is_liked = is_liked,
                is_bookmarked = is_bookmarked,
            ))

        # 사전 형식으로 전달 { key(템플릿으로 전달할 이름) : value }
        return render(
            request, "kinsta/main.html", context=dict(feeds=feed_list, user=login_user)
        )


# from uuid import uuid4
# import os
# from kinsta.settings import MEDIA_ROOT


class upload_feed(APIView):
    def post(self, request):
        
        file = request.FILES["file"]

        # 파일 이름을 고유한 id로 변경 (프로그램에서 다루기 쉽게)
        uuid_name = uuid4().hex + ".jpg"
        # /MEDIA_ROOT/uuid_name로 이미지 저장
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        # 파일 저장
        with open(save_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        content = request.data.get("content")
        img_location = uuid_name

        print(file)
        print(uuid_name)
        print(content)

        Feed.objects.create(
            image=img_location,
            content=content,
            user_email = request.session['email']
        )

        return Response(status=200)

# 피드 삭제
class DeleteFeed(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id')
        try:
            record_list = Feed.objects.filter(id = feed_id)
            record_list.delete()
        except:
            print("삭제 에러 발생")
            return Response(status=500)
        return Response(status=200)

from django.shortcuts import get_object_or_404

class profile(APIView):
    def get(self, request):  # get 요청이 왔을 때
        print("profile 접속")
        try:
            user_email = request.session["email"]
        except KeyError:
            print("세션 비어있음")
            return render(request, "user/login.html")

        login_user = user.objects.filter(user_email=user_email).first()  # 유저 정보
        print("유저 닉네임 :", login_user.user_nickname)
        #

        # 사전 형식으로 전달 { key(템플릿으로 전달할 이름) : value }
        return render(request, "content/profile.html", context=dict(user=login_user))

    # 프로필 변경
    def post(self, request):        
        try:
            print("사용자 접속 확인")
            email = request.session["email"]
        except:
            print("프로필 변경 오류 발생")
            return render(request, "user/login.html")
            
        profile_img = request.FILES["profile_img"]
        print("변경될 이미지 :", profile_img)

        # 랜덤 파일명
        uuid_name = uuid4().hex + ".jpg"
        # /media에 저장
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        # 파일 읽기
        with open(save_path, "wb+") as destination:
            for chunk in profile_img.chunks():
                destination.write(chunk)
                
        
        print("접속 중인 사람 :", email)
        u = get_object_or_404(user, user_email = email)        
        u.profile_img = uuid_name
        u.save()

        return render(request, "content/profile.html")

class upload_comment(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id')
        comment_content = request.data.get('comment_content')
        email = request.session["email"]
        login_user = user.objects.filter(user_email=email).first()
        
        comment.objects.create(feed_id = feed_id,
                               email = email,
                               comment_content = comment_content,
                               nickname = login_user.user_nickname)
        
        return Response(status=200)
    
class TogleLike(APIView):
    def post(self, requeset):
        feed_id = requeset.data.get('feed_id')
        is_like = requeset.data.get('is_like')
        
        if is_like == 'true':
            is_like = False
        else:
            is_like = True
        
        email = requeset.session['email']
        nickname = requeset.session['nickname']
        
        like_user = like.objects.filter(feed_id = feed_id, email = email).first()        
        
        # 좋아요 누른적이 없음
        if like_user is None:
            like.objects.create(
                feed_id = feed_id,
                email = email,
                nickname = nickname,
                is_like = is_like
            )
        # 좋아요 누른적이 있음
        else:
            if like_user.is_like:
                like_user.is_like = False
            else:
                like_user.is_like = True
                
            like_user.save()                
        
        return Response(status=200)
    
class TogleBookmark(APIView):
    def post(self, requeset):
        feed_id = requeset.data.get('feed_id')
        is_bookmark = requeset.data.get('is_bookmark')
        
        if is_bookmark == 'true':
            is_bookmark = False
        else:
            is_bookmark = True
        
        email = requeset.session['email']
        nickname = requeset.session['nickname']
        
        bookmark_user = bookmark.objects.filter(feed_id = feed_id, email = email).first()        
        
        # 북마크 누른적이 없음
        if bookmark_user is None:
            bookmark.objects.create(
                feed_id = feed_id,
                email = email,
                nickname = nickname,
                is_bookmark = is_bookmark
            )
        # 북마크 누른적이 있음
        else:
            if bookmark_user.is_bookmark:
                bookmark_user.is_bookmark = False
            else:
                bookmark_user.is_bookmark = True
                
            bookmark_user.save()                
        
        return Response(status=200)