from django.shortcuts import render
from rest_framework.views import APIView

# def index(request):
#     return render(request, 'index.html')

class sub(APIView):
    def get(self, request): # get 요청이 왔을 때
        return render(request, "kinsta/index.html")
    
class member(APIView):
    def get(self, request):
        return render(request, 'kinsta/membership.html')
    
# class main(APIView):
#     def get(self, request):
#         return render(request, 'kinsta/main.html')