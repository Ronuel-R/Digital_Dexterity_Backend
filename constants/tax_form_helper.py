from digital_dex_admin_web.models.tax_form_model import TaxForm

class TaxFormHelper:
    def validate_fields(self,request):
        errors = {}
        
        if 'td_no' in request.data and request.data['td_no'] == '':
            errors['td_no'] =  'Tax Declaration Number should not be empty'
        
        if request.data['td_no'] and TaxForm.objects.filter(td_no=request.data["td_no"]).count() != 0:
            errors['td_no'] = 'Tax Declaration Number is already used'

        if 'property_identification_no' in request.data and request.data['property_identification_no'] == '':
            errors['property_identification_no'] =  'Property Identification number should not be empty'

        if request.data['property_identification_no'] and TaxForm.objects.filter(td_no=request.data["property_identification_no"]).count() != 0:
            errors['property_identification_no'] = 'Property Identification number is already used'
        
        ############## OWNER ########################

        if 'owner' in request.data and request.data['owner'] == '':
            errors['owner'] =  'Owner should not be empty'

        if 'owner_tin' in request.data and request.data['owner_tin'] == '':
            errors['owner_tin'] =  'Owner Tin should not be empty'

        if 'owner_address' in request.data and request.data['owner_address'] == '':
            errors['owner_address'] =  'Owner Address should not be empty'

        if 'owner_tel_no' in request.data and request.data['owner_tel_no'] == '':
            errors['owner_tel_no'] =  'Owner Telephone number should not be empty'
        
        ############## Admin ####################
        if 'administrator_beneficial_user' in request.data and request.data['administrator_beneficial_user'] == '':
            errors['administrator_beneficial_user'] =  'Administrator Beneficial User should not be empty'

        if 'admin_tin' in request.data and request.data['admin_tin'] == '':
            errors['admin_tin'] =  'Admin Tin should not be empty'
        
        if 'admin_address' in request.data and request.data['admin_address'] == '':
            errors['admin_address'] =  'Admin Address should not be empty'
        
        if 'admin_tel_no' in request.data and request.data['admin_tel_no'] == '':
            errors['admin_tel_no'] =  'Admin Telephone number should not be empty'

        ############## PROPERTY ##################
        if 'property_location' in request.data and request.data['property_location'] == '':
            errors['property_location'] =  'Property Location should not be empty'

        if 'oct_no' in request.data and request.data['oct_no'] == '':
            errors['oct_no'] =  'OCT number should not be empty'

        if 'survey_no' in request.data and request.data['survey_no'] == '':
            errors['survey_no'] =  'Survey number should not be empty'

        if 'cct' in request.data and request.data['cct'] == '':
            errors['cct'] =  'CCT should not be empty'

        if 'lot_no' in request.data and request.data['lot_no'] == '':
            errors['lot_no'] =  'Lot number should not be empty'

        if 'dated' in request.data and request.data['dated'] == '':
            errors['date'] =  'Date should not be empty'

        if 'blk_no' in request.data and request.data['blk_no'] == '':
            errors['blk_no'] =  'Block number should not be empty'

        ############## BOUNDARY ###################
        if 'north' in request.data and request.data['north'] == '':
            errors['north'] =  'North Field should not be empty'

        if 'west' in request.data and request.data['west'] == '':
            errors['west'] =  'West Field should not be empty'

        if 'east' in request.data and request.data['east'] == '':
            errors['east'] =  'East Field should not be empty'

        if 'south' in request.data and request.data['south'] == '':
            errors['south'] =  'South Field should not be empty'

        ############## KIND OF PROPERTY ############

        if 'property_choices' in request.data and request.data['property_choices'] == '':
            errors['property_choices'] =  'Please select an appropriate property type'

        ############# FINAL ASSESSMENT ############

        if 'taxable' in request.data and request.data['taxable'] == '':
            errors['taxable'] =  'Please select from the choices'

        ############# EFFECTIVITY OF ASSESSMENT ############

        if 'qtr' in request.data and request.data['qtr'] == '':
            errors['qtr'] =  'Quarter should not be empty'

        if 'year' in request.data and request.data['year'] == '':
            errors['year'] =  'Year should not be empty'

        if 'date_assessed' in request.data and request.data['date_assessed'] == '':
            errors['date_assessed'] =  'Date should not be empty'

        return errors
