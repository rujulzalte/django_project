from django.shortcuts import render
from django.http import HttpResponse
from . models import UserLogin
from django.http import HttpResponse, JsonResponse
from . serializers import UserLoginSerial
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def Homepage(request):
    all_object = UserLogin.objects.all()
    print(all_object)
    return render(request,'Login/homepage.html', context = all_object)
    #return render(request, 'Login/homepage.html')

@csrf_exempt
def Alldata(request,pk):
    try:
        data = UserLogin.objects.get(pk=pk)
    except:
        return HttpResponse("Sorry!! Not Found",status = 404)

    if request.method == 'GET':
        user = UserLoginSerial(data)
        print(user)
        return JsonResponse(user.data, status = 200)
    
    if request.method == 'POST':
        input_data = JSONParser().parse(request)
        serializer = UserLoginSerial(data = input_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        else:
            return HttpResponse("Error", status = 400)
    
    elif request.method == 'PUT':
        new_data = JSONParser().parse(request)
        serializer = UserLoginSerial(data,data = new_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        else:
            return HttpResponse("Error", status = 400)
        
    elif request.method == 'DELETE':
        data.delete()
        return HttpResponse("Deleted", status = 204)

def get(request):
    try:
        all_data = UserLogin.objects.all()
    except:
        return HttpResponse("Sorry!! Not Found",status = 404)

    if request.method == 'GET':
        user = UserLoginSerial(all_data, many = True)
        print(user)
        return JsonResponse(user.data, safe = False)