from rest_framework.views import APIView
from .......models.ownership_record_model import OwnsershipRecordCardModel
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class DeleteOwnershipRecordCardViews(APIView):

    def post(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None

        # token = AuthUser.get_token(request)

        # if type(token) == dict:
        #     return Response(token)

        # payload = AuthUser.get_user(token)

        # if 'errors' in payload:
        #     return Response(payload)

        # errors = PermissionChecker.validate_permission_delete(self,payload)

        # if len(errors) != 0:
        #     status = bad_request
        #     message = 'Invalid Input'
        #     return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        if "id" in request.query_params:
            id = request.query_params["id"]
            try:
                tax_model = OwnsershipRecordCardModel.objects.get(id=id)
            except ObjectDoesNotExist:
                message = 'Ownership Record Card with id {} does not exist'.format(id)
                status_code = bad_request
                return Response({"status": status_code, "message": message, "data": data, "errors": errors})

            tax_model.delete()

            message = 'Successfuly Deleted'
            status = ok
        else:
            message = 'Invalid Format'
            status = bad_request
        return Response({"status": status , "message": message , "data": data, "errors":errors})