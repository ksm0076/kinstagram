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
        profile_img = "default_profile.jpg"
        email = request.data.get("user_email")
        user_name = request.data.get("user_name")
        user_nickname = request.data.get("user_nickname")
        user_password = request.data.get("user_password")

        if user.objects.filter(user_email=email).exists():
            return JsonResponse({"success": False, "error": "이메일이 중복되었습니다."})
        
        if user.objects.filter(user_nickname = user_nickname).exists():
            return JsonResponse({"success": False, "error": "닉네임이 중복되었습니다."})

        u = user.objects.create(
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
        user_email = request.data.get("user_email")
        user_password = request.data.get("user_password")
        
        login_user = user.objects.filter(user_email = user_email).first()
        
        if login_user == None:
            print("존재하지 않는 사용자 접근")
            # return JsonResponse({"success" : False, "error" : "회원정보가 잘못되었습니다."})
            return JsonResponse({"success" : False, "error" : "존재하지 않는 회원입니다."})
        
        # 로그인 성공
        if login_user.check_password(user_password):
            request.session['email'] = user_email
            return JsonResponse({"success" : True})
        else:
            # return JsonResponse({"success" : False, "error" : "회원정보가 잘못되었습니다."})
            return JsonResponse({"success" : False, "error" : "비밀번호가 잘못되었습니다."})
