from digital_dex_admin_web.models.tax_map_control_model import TaxMapControl
from digital_dex_admin_web.models.assessment_model import Assessment

class TaxMapControlHelper:
    def validate_fields(self, request):
        errors = {}
        
        if 'prov_city' in request.data and request.data['prov_city'] == '':
            errors['prov_city'] = 'Province/City should not be empty'

        if 'prov_city_index_no' in request.data and request.data['prov_city_index_no'] == '':
            errors['prov_city_index_no'] = 'Province/City Index Number should not be empty'

        if request.data['prov_city_index_no'] and TaxMapControl.objects.filter(prov_city_index_no=request.data["prov_city_index_no"]).count() != 0:
            errors['prov_city_index_no'] = 'Province/City Index Number is already used'


        if 'mun_city' in request.data and request.data['mun_city'] == '':
            errors['mun_city'] = 'Municipality/City should not be empty'

        if 'mun_city_index_no' in request.data and request.data['mun_city_index_no'] == '':
            errors['mun_city_index_no'] = 'Municipality/City Index Number should not be empty'

        if request.data['mun_city_index_no'] and TaxMapControl.objects.filter(mun_city_index_no=request.data["mun_city_index_no"]).count() != 0:
            errors['mun_city_index_no'] = 'Municipality/City Index Number is already used'
    

        if 'barangay' in request.data and request.data['barangay'] == '':
            errors['barangay'] = 'Barangay should not be empty'

        if 'barangay_index_no' in request.data and request.data['barangay_index_no'] == '':
            errors['barangay_index_no'] = 'Barangay Index Number should not be empty'

        if request.data['barangay_index_no'] and TaxMapControl.objects.filter(barangay_index_no=request.data["barangay_index_no"]).count() != 0:
            errors['barangay_index_no'] = 'Barangay Index Number is already used'


        if 'section_index_no' in request.data and request.data['section_index_no'] == '':
            errors['section_index_no'] = 'Section Index Number should not be empty'

        if request.data['section_index_no'] and TaxMapControl.objects.filter(section_index_no=request.data["section_index_no"]).count() != 0:
            errors['section_index_no'] = 'Section Index Number is already used'

        
        if 'assessors_lot_no' in request.data and request.data['assessors_lot_no'] == '':
            errors['assessors_lot_no'] = 'Assessor\'s Lot Number should not be empty'

        if request.data['assessors_lot_no'] and Assessment.objects.filter(assessors_lot_no=request.data["assessors_lot_no"]).count() != 0:
            errors['assessors_lot_no'] = 'Assessor\'s Lot Number is already used'


        if 'survey_lot_no' in request.data and request.data['survey_lot_no'] == '':
            errors['survey_lot_no'] = 'Survey Lot Number should not be empty'

        if request.data['survey_lot_no'] and Assessment.objects.filter(survey_lot_no=request.data["survey_lot_no"]).count() != 0:
            errors['survey_lot_no'] = 'Survey Lot Number is already used'


        if 'land_title_no' in request.data and request.data['land_title_no'] == '':
            errors['land_title_no'] = 'Land Title Number should not be empty'

        if request.data['land_title_no'] and Assessment.objects.filter(land_title_no=request.data["land_title_no"]).count() != 0:
            errors['land_title_no'] = 'Land Title Number is already used'


        if 'land_area' in request.data and request.data['land_area'] == '':
            errors['land_area'] = 'Land Area should not be empty'

        if 'land_class_code' in request.data and request.data['land_class_code'] == '':
            errors['land_class_code'] = 'Land Class Code should not be empty'

        if 'name_of_owner' in request.data and request.data['name_of_owner'] == '':
            errors['name_of_owner'] = 'Name of Owner should not be empty'

        if 'arp_no' in request.data and request.data['arp_no'] == '':
            errors['arp_no'] = 'ARP Number should not be empty'

        if request.data['arp_no'] and Assessment.objects.filter(arp_no=request.data["arp_no"]).count() != 0:
            errors['arp_no'] = 'ARP Number is already used'


        if 'td_no' in request.data and request.data['td_no'] == '':
            errors['td_no'] = 'Tax Declaration Number should not be empty'

        if request.data['td_no'] and Assessment.objects.filter(td_no=request.data["td_no"]).count() != 0:
            errors['td_no'] = 'Tax Declaration Number is already used'


        if 'building_structure' in request.data and request.data['building_structure'] == '':
            errors['building_structure'] = 'Building/Structure should not be empty'

        if 'machinery' in request.data and request.data['machinery'] == '':
            errors['machinery'] = 'Machinery should not be empty'

        if 'others' in request.data and request.data['others'] == '':
            errors['others'] = 'Other Information should not be empty'

        if 'remarks' in request.data and request.data['remarks'] == '':
            errors['remarks'] = 'Remarks should not be empty'

        return errors