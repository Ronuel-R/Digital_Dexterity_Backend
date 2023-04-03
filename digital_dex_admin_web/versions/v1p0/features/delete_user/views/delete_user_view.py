from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers

class DeleteUserView(APIView):
    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")

    def delete_user(self, username):
        user = User.objects.get(username=username)
        user.delete()

    def post(self, request):
        errors = {}
        data = {}
        status_code = None
        message = None
        
        if not request.user.is_authenticated:
            errors["authentication"] = ["You are not logged in."]
            status_code = status.HTTP_401_UNAUTHORIZED
        else:
            username = request.data.get('username')
            if not username:
                errors["username"] = ["This field is required."]
                status_code = status.HTTP_400_BAD_REQUEST
            else:
                try:
                    self.validate_username(username)
                except serializers.ValidationError as e:
                    errors = e.detail
                    status_code = status.HTTP_400_BAD_REQUEST
                else:
                    self.delete_user(username)
                    message = "User deleted successfully."
                    status_code = status.HTTP_200_OK
        
        if errors:
            status_code = status_code or status.HTTP_400_BAD_REQUEST
            return Response({"status": status_code, "message": message, "data": data, "errors": errors})
        elif message:
            return Response({"status": status_code, "message": message, "data": data, "errors": errors})
        else:
            return Response({"status": status_code, "message": message, "data": data, "errors": errors})