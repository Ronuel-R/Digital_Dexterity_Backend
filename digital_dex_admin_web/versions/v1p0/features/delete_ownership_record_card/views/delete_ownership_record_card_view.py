from rest_framework.views import APIView
from ......models.ownership_record_model import OwnsershipRecordCardModel
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from constants.http_messages import *

class DeleteOwnershipRecordCardViews(APIView):

    def post(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None

        if not request.user.is_authenticated:
            message = 'You are not logged in'
            status = unauthorized
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        
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