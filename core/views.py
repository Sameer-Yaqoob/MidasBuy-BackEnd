from django.shortcuts import render
from rest_framework.decorators import APIView
from urllib.error import HTTPError
from core.models import User
from core.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.permissions import AllowAny

# from django.contrib.auth import authentication, login, logout
# from django.contrib import messages



# Create your views here.
# def call_back_view(request,*args,**kwargs):
#     print("request",request)
#     print("args",args)
#     print("kwargs",kwargs)
#     return render(request,'core/call_back.html',{})

# class Me(APIView):
#     def get(self,request):
#         auth_user = request.auth_user
#         if auth_user is None or (auth_user and not hasattr(auth_user, 'id')):
#             raise HTTPError(None, 404, "User Account missing", None, None)
#         user = User.objects.get(id=auth_user.id)
#         data = MeSerializer(user).data
#         return Response(data, status=status.HTTP_200_OK)   


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    permissions_classes = [AllowAny]

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'expiration': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'creation': datetime.datetime.utcnow(),
        }
    # .decode('utf-8')
        token = jwt.encode(payload, 'secret', algorithm='HS256', json_encoder=DjangoJSONEncoder)
        # print("token", token.decode("utf-8",'strict'))

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            'user_email':user.email,
            'user_username':user.username,
            'message': "success"
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


