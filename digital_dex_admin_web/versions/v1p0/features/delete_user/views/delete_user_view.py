from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from constants.http_messages import *

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
        status = None
        message = None
        
        if not request.user.is_authenticated:
            message = 'You are not logged in'
            status = unauthorized
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        
        else:
            username = request.data.get('username')
            if not username:
                errors["username"] = ["This field is required."]
                status = bad_request
            else:
                try:
                    self.validate_username(username)
                except serializers.ValidationError as e:
                    errors = e.detail
                    status = bad_request
                else:
                    self.delete_user(username)
                    message = "User deleted successfully."
                    status = ok
        
        if errors:
            status = status or bad_request
            return Response({"status": status, "message": message, "data": data, "errors": errors})
        elif message:
            return Response({"status": status, "message": message, "data": data, "errors": errors})
        else:
            return Response({"status": status, "message": message, "data": data, "errors": errors})