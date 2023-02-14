from django.shortcuts import render,HttpResponse
from .serializers import blogser,likeser,userser
from . models import blog,likes
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
# from rest_framework.generics import ListAPIView
# Create your views here.

from rest_framework.decorators import api_view,authentication_classes,permission_classes

from rest_framework.response import Response




#blog i have given acces for owner can see how many post he have and like of the post and created API for CRUD operation

#please look at the code...
#  thank you!.

@api_view(['POST','GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def blob(request):
    if request.method=='GET':
        use=request.user
        stu=blog.objects.filter(user=use)
        ser=blogser(stu,many=True)
        return Response({'data':ser.data})
    if request.method=='POST':
        stu=blogser(data=request.data)
        # blogser.validated_data['user']=request.user
        if stu.is_valid():
            # blogser.validated_data['user']=request.user
            # print(blogser.validated_data['user'])
            stu.save()
            return Response({'data':stu.data})
        return Response({'data':stu.errors})
@api_view(['PUT','PATCH','DELETE','GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def blob1(request,pk):
    if request.method=='GET':
            use=request.user
            stu=blog.objects.get(id=pk)
            ser=blogser(stu)
            return Response({'data':ser.data})
    if request.method=='PUT':
        stu=blog.objects.get(id=pk)
        ser=blogser(stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data})
        return Response({'data':ser.errors})
    if request.method=='PATCH':
        stu=blog.objects.get(id=pk)
        ser=blogser(stu,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data})
        return Response({'data':ser.errors})
    if request.method=='DELETE':
        stu=blog.objects.get(id=pk)
        stu.delete()
        return Response({'respone':' succsessfuly delted!'})





#i given the owner of the account he can only have the acces for his likes with CRUD operation

#Than you!..


@api_view(['POST','GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def like(request):
    if request.method=='GET':
        use=request.user
        stu=likes.objects.filter(user=use)
        ser=likeser(stu,many=True)
        return Response({'data':ser.data})
    if request.method=='POST':
        ser=likeser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data})
        return Response({'data':ser.erroe})

@api_view(['PUT','PATCH','DELETE','GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def like1(request,pk):
    if request.method=='GET':
        use=request.user
        stu=likes.objects.get(id=pk)
        ser=likeser(stu)
        return Response({'data':ser.data})
    if request.method=='PUT':
        stu=likes.objects.get(id=pk)
        ser=likeser(stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data})
        return Response({'data':ser.errors})
    if request.method=='PATCH':
        stu=likes.objects.get(id=pk)
        ser=likeser(stu,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data})
        return Response({'data':ser.errors})
    if request.method=='DELETE':
        stu=likes.objects.get(id=pk)
        stu.delete
        return Response({'response':'delete record successfully!'})






#this is the who is owner of the account he can have the acces he can only do the changes

#Than you!..


@api_view(['PUT','PATCH','DELETE','GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def owner(request):
    if request.method=='GET':
        pk=request.user.id
        # use=User.objects.filter(username=use)
        # pk=User.objects.filter(username=use).values_list('id', flat=True)
        use=User.objects.get(id=pk)
        print(use1)
        ser=userser(use)
        return Response({'data':ser.data})
    if request.method=='PUT':
        pk=request.user.id
        stu=User.objects.get(id=pk)
        ser=userser(stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data})
        return Response({'data':ser.errors})
    if request.method=='PATCH':
        pk=request.user.id
        stu=User.objects.get(id=pk)
        ser=userser(stu,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data})
        return Response({'data':ser.errors})
    if request.method=='DELETE':
        pk=request.user.id
        stu=User.objects.get(id=pk)
        stu.delete()
        return Response({'data':'your successfuly delted!.'})






#this api is work like ADMIN like all user data you can acces with this api normal user not able to acces
#this api who are the superuser and staff and superuser have check mark he can only acces this permissions


#owner of account he can modify his data him selt i have created one api above look at that name of the function is  "owner"
#Than you!..



@api_view(['POST','GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def use(request):
    if request.method=='GET':
        stu=User.objects.all()
        ser=userser(stu,many=True)
        return Response({'data':ser.data})
    if request.method=='POST':
        ser=userser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data})
        return Response({'data':ser.error})

@api_view(['PUT','PATCH','DELETE','GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def use1(request,pk):
    if request.method=='GET':
        use=request.user
        stu=User.objects.get(id=pk)
        ser=userser(stu)
        return Response({'data':ser.data})
    
    if request.method=='PUT':
        stu=User.objects.get(id=pk)
        ser=userser(stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data':ser.data})
        return Response({'data':ser.errors})
    if request.method=='PATCH':
        stu=User.objects.get(id=pk)
        ser=userser(stu,data=request.data,partial=True)
        return Response({'data':ser.data})
    if request.method=='DELETE':
        stu=User.objects.get(id=pk)
        stu.delete()
        return Response({'data':'delted successfully the user!'})





