from rest_framework.views import APIView
from .......models.ownership_record_model import OwnsershipRecordCardModel
from ..serializers.display_ownership_record_card_serializer import DisplayOwnershipRecordCardSerializer
from rest_framework.response import Response
from constants.http_messages import *

class DisplayOwnershipRecordCardViews(APIView):

    def get(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None

        # if not request.user.is_authenticated:
        #     message = 'You are not logged in'
        #     status = unauthorized
        #     return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        
        try: 
            id = request.query_params["id"]
            tax = OwnsershipRecordCardModel.objects.filter(id = id).first()

            if tax is None:
                message = 'Ownership Record Card does not exist'
                status = not_found
                return Response({"status": status , "message": message , "data": data, "errors":errors})

            serializer = DisplayOwnershipRecordCardSerializer(tax)
        except:
            tax = OwnsershipRecordCardModel.objects.all()
            serializer = DisplayOwnershipRecordCardSerializer(tax,many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message , "data": data, "errors":errors})