from django.shortcuts import render
from rest_framework.views import APIView
from .models import user
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse


# Create your views here.
class signup(APIView):
    def get(self, request):
        return render(request, "user/signup.html")  # html 파일 위치

    def post(self, request):
        profile_img = "media/default_profile.jpg"
        email = request.data.get("user_email")
        user_name = request.data.get("user_name")
        user_nickname = request.data.get("user_nickname")
        user_password = request.data.get("user_password")

        if user.objects.filter(user_email=email).exists():
            return JsonResponse({"success": False, "error": "이메일이 중복되었습니다."})
        
        if user.objects.filter(user_nickname = user_nickname).exists():
            return JsonResponse({"success": False, "error": "닉네임이 중복되었습니다."})

        user.objects.create(
            profile_img=profile_img,
            user_email=email,
            user_name=user_name,
            user_nickname=user_nickname,
            password=make_password(user_password),
        )
        return JsonResponse({'success' : True})


class login(APIView):
    def get(self, request):
        return render(request, "user/login.html")  # html 파일 위치

    def post(self, request):
        pass
