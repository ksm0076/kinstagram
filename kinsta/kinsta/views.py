from django.shortcuts import render
from rest_framework.views import APIView

def index(request):
    return render(request, 'index.html')


# class sub(APIView):
#     def get(self, request):
#         return render(request, "kinsta/index.html")