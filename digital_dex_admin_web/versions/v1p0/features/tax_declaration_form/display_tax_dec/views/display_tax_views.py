from rest_framework.views import APIView

################### Models ##########################
from .......models.tax_form_model import TaxForm
from ...create_tax_form.serializers.tax_form_serializer import TaxFormSerializer
from ..serializers.display_tax_serializer import DisplayTaxFormSerializer
from .......models.tax_initial_assessment_model import InitialAssessment
################### Static Modules ######################

from rest_framework.response import Response
from constants.http_messages import *

class DisplayTaxDecViews(APIView):

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
            tax = TaxForm.objects.filter(id = id).first()

            if tax is None:
                message = 'Tax Declaration Form does not exist'
                status = not_found
                return Response({"status": status , "message": message , "data": data, "errors":errors})

            serializer = DisplayTaxFormSerializer(tax)
        except:
            tax = TaxForm.objects.all()
            serializer = DisplayTaxFormSerializer(tax,many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message , "data": data, "errors":errors})