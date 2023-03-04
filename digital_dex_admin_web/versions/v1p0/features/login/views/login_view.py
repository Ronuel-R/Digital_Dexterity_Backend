from rest_framework.views import APIView
from ..serializers.login_serializer import LoginAdminSerializer
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework import status
from django.contrib.auth.models import User


class LoginAdminView(APIView):
    serializer_class = LoginAdminSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        
        errors = self.validate_email_and_password(email, password)
        
        if errors:
            return Response({'errors': errors}, status=status.HTTP_401_UNAUTHORIZED)
        

        user = self.authenticate_user(email, password)
        if user:
            login(request, user)
            return Response({'data': {'message': 'Logged in successfully.'}}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'authentication': ['Invalid email or password.']}}, status=status.HTTP_401_UNAUTHORIZED)


    def validate_email_and_password(self, email, password):
        errors = {}
        if not email:
            errors['email'] = ['Email is required.']
        if not password:
            errors['password'] = ['Password is required.']
        if email and not User.objects.filter(email=email).exists():
            errors['email'] = ['Invalid email.']
        if password and email and not self.authenticate_user(email, password):
            errors['password'] = ['Invalid password.']

        return errors


    def authenticate_user(self, email, password):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if not user.check_password(password):
            return None

        return user
    
    
class LogoutAdminView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'You are not logged in.'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            logout(request)
            return Response({'data': {'message': 'Logged out successfully.'}}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    