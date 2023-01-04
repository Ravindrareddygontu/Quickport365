from service.serializers import *
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed, NotAcceptable, ValidationError
from rest_framework.response import Response
import jwt
import requests
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.contrib.auth import login, logout
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class ParcelDetailsdetails(ModelViewSet):
    queryset = ParcelDetails.objects.all()
    serializer_class = ParcelDetailsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AdminDriverView(ModelViewSet):
    queryset = Admin_driver.objects.all()
    serializer_class = Admin_driverSerializer


class Orderdetails(ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer


class Drivers_ordersView(ModelViewSet):
    queryset = Drivers_orders.objects.all()
    serializer_class = Drivers_ordersSerializer


class ComplaintView(ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer


class Signup(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        user = User.objects.filter(username=username).first()
        print(user.is_superuser)
        user.set_password(password)
        if user is not None:
            if user.check_password(password):
                print('hiii')
                login(request, user)
                return Response('login successful')
            else:
                raise AuthenticationFailed('Incorrect Password')
        else:
            raise AuthenticationFailed('user not found')

        # payload = {
        #     'id': user.id,
        #     'exp': datetime.utcnow()+timedelta(minutes=5),
        #     'iat': datetime.utcnow()
        # }
        # token = jwt.encode(payload, 'secret', algorithm='HS256')
        # response = Response()
        # response.set_cookie(key='jwt', value=token, httponly=True)
        # print(request.COOKIES)
        # response.data = {
        #     'jwt': token
        # }


class UserView(APIView):
    def get(self, request):
        print(request.COOKIES)
        token = request.COOKIES.get('jwt')
        print(token, '--------')
        if not token:
            print('no=======')
            raise AuthenticationFailed('Unauthenticated User')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e:
            print(e,'yes------------')
            raise AuthenticationFailed('Unauthenticated user')

        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class PincodeView(APIView):
    def post(self, request):
        origin_pin = request.data.get('origin_pincode')
        destination_pin = request.data.get('destination_pincode')
        origin = requests.get(f"https://api.postalpincode.in/pincode/{origin_pin}").json()
        destination = requests.get(f"https://api.postalpincode.in/pincode/{destination_pin}").json()
        print(destination)
        if destination[0]['Status'] != 'Error' and origin[0]['Status'] != 'Error':
            return Response('success')
        else:
           raise ValidationError('incorrect pincodes')
