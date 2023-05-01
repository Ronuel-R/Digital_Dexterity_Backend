from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from constants.http_messages import *
from constants.auth_user import AuthUser

class DeleteUserView(APIView):
    def validate_id(self, payload):
        try:
            User.objects.get(id=payload['id'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")

    def delete_user(self, payload):
        user = User.objects.get(id=payload['id'])
        user.delete()

    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None
        
        token = AuthUser.get_token(request)

        if type(token) == dict:
            return Response(token)

        payload = AuthUser.get_user(token)

        if 'errors' in payload:
            return Response(payload)
        
        id = payload['id']
        if not id:
            errors["id"] = ["This field is required."]
            status = bad_request
        else:
            try:
                self.validate_id(payload)
            except serializers.ValidationError as e:
                errors = e.detail
                status = bad_request
            else:
                self.delete_user(payload)
                message = "User deleted successfully."
                status = ok
        
        if errors:
            status = status or bad_request
            return Response({"status": status, "message": message, "data": data, "errors": errors})
        elif message:
            return Response({"status": status, "message": message, "data": data, "errors": errors})
        else:
            return Response({"status": status, "message": message, "data": data, "errors": errors})