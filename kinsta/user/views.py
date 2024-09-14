from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import user
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse


# Create your views here.
class signup(APIView):
    def get(self, request):
        return render(request, "user/signup.html")  # html 파일 위치

    def post(self, request):
        profile_img = "default_profile.jpg"
        email = request.data.get("user_email")
        user_name = request.data.get("user_name")
        user_nickname = request.data.get("user_nickname")
        user_password = request.data.get("user_password")

        if user.objects.filter(user_email=email).exists():
            return JsonResponse({"success": False, "error": "이메일이 중복되었습니다."})

        if user.objects.filter(user_nickname=user_nickname).exists():
            return JsonResponse({"success": False, "error": "닉네임이 중복되었습니다."})

        u = user.objects.create(
            profile_img=profile_img,
            user_email=email,
            user_name=user_name,
            user_nickname=user_nickname,
            password=make_password(user_password),
        )

        return JsonResponse({"success": True})


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password


class login(APIView):
    def get(self, request):
        try:
            request.session["email"]
            return redirect("main")
        except KeyError:
            print("세션 비어있음")
            return render(request, "user/login.html")

    def post(self, request):
        user_email = request.data.get("user_email")
        user_password = request.data.get("user_password")

        login_user = user.objects.filter(user_email=user_email).first()

        ##
        if login_user == None:
            print("존재하지 않는 사용자 접근")
            # return JsonResponse({"success" : False, "error" : "회원정보가 잘못되었습니다."})
            return JsonResponse(
                {"success": False, "error": "존재하지 않는 회원입니다."}
            )

        # 로그인 성공
        if login_user.check_password(user_password):
            # 세션 생성
            request.session["email"] = user_email
            request.session["nickname"] = login_user.user_nickname
            return JsonResponse({"success": login_user.user_nickname})
        else:
            # return JsonResponse({"success" : False, "error" : "회원정보가 잘못되었습니다."})
            return JsonResponse(
                {"success": False, "error": "비밀번호가 잘못되었습니다."}
            )


class logout(APIView):
    def get(self, request):
        # 세션 삭제
        request.session.clear()
        print("세션 삭제")
        return redirect("login")


from django.shortcuts import get_object_or_404
from uuid import uuid4
import os

from content.models import Feed, bookmark
from kinsta.settings import MEDIA_ROOT

class Profile(APIView):
    def get(self, request):  # get 요청이 왔을 때
        print("profile 접속")
        try:
            user_email = request.session["email"]
        except KeyError:
            print("세션 비어있음")
            return redirect("login")

        login_user = user.objects.filter(user_email=user_email).first()  # 유저 정보
        print("유저 닉네임 :", login_user.user_nickname)
        #
        feed_object_list = Feed.objects.filter(user_email=user_email).order_by("-id")
        feed_list = []

        for feed in feed_object_list:
            feed_list.append(
                dict(
                    feed_id=feed.id,
                    feed_img=feed.image,
                )
            )            
        
        
        
        
        
        bookmark_id_list = list(bookmark.objects.filter(email=user_email, is_bookmark = 1).values_list('feed_id', flat=True))
        bookmark_id_list = sorted(bookmark_id_list, reverse=True)
        
        bookmark_list = []
        
        for feed_id in bookmark_id_list:
            bookmark_feed = Feed.objects.filter(id = feed_id).first()
            bookmark_list.append(
                dict(
                    bookmark_feed_id = feed_id,
                    feed_img = bookmark_feed.image,
                )
            )
        # 사전 형식으로 전달 { key(템플릿으로 전달할 이름) : value }
        return render(
            request,
            "user/profile.html",
            context=dict(
                user=login_user, feeds=feed_list, feed_num=len(feed_object_list), bookmarks = bookmark_list
            ),
        )

    # 프로필 변경
    def post(self, request):
        try:
            print("사용자 접속 확인")
            email = request.session["email"]
        except:
            print("프로필 변경 오류 발생")
            return redirect("login")

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
        u = get_object_or_404(user, user_email=email)
        u.profile_img = uuid_name
        u.save()

        return render(request, "user/profile.html")