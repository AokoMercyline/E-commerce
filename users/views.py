# from django.shortcuts import render
from rest_framework import generics, permissions,status
from django.contrib.auth.models import User
from rest_framework import viewsets
from  .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer, ProductSerializer
from knox.models import AuthToken
from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated
# from .decorators import admin_hr_required, admin_only
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from .models import Product

class UserSerializer(viewsets.ModelViewSet):
    # api endpoint that allows users to be viewed or edited
    queryset = User.objects.all().order_by()
    serializer_class = UserSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context).data,
        "token": AuthToken.objects.create(user)[1]
        })
        
class UserProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        profile_serializer = UserProfileSerializer(UserProfile)
        return Response(profile_serializer.data)
    
    
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
    
class UserListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   


# class CustomSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         if request.query_params.get('title_only'):
#             return ['title']
#         return super(CustomSearchFilter, self).get_search_fields(view, request)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
    
    
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
    
 
# Change Password 
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']

    