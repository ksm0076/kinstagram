from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class signup(APIView):
    def get(self, request):
        return render(request, 'user/signup.html') # html 파일 위치
    
class login(APIView):
    def get(self, request):
        return render(request, 'user/login.html') # html 파일 위치