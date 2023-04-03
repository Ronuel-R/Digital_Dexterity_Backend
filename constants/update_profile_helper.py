import re
from digital_dex_admin_web.models.admin_model import Admin
from django.contrib.auth.models import User


class UpdateHelper:
    def validate_fields(self, request):
        errors = {}

        if 'user' in request.data and request.data['user'] == '':
            errors['user'] = 'User should not be empty'
        if 'user' in request.data and User.objects.filter(username=request.data['user']).exists():
            errors['user'] = 'This username is already taken'


        if 'email' in request.data and not re.match(r"[^@]+@[^@]+\.[^@]+", request.data['email']):
            errors['email'] = 'Invalid email format'
        if 'email' in request.data and User.objects.filter(email=request.data['email']).exists():
            errors['email'] = 'This email is already taken'
            

        if request.data['first_name'] != '':
            if 'first_name' in request.data and User.objects.filter(first_name=request.data['first_name']).exists():
                errors['first_name'] = 'This first name is already taken'

        if request.data['last_name'] != '':
            if 'last_name' in request.data and User.objects.filter(last_name=request.data['last_name']).exists():
                errors['last_name'] = 'This last name is already taken'


        if 'full_name' in request.data and request.data['full_name'] == '':
            errors['full_name'] = 'Full name should not be empty'
        if 'full_name' in request.data and Admin.objects.filter(full_name=request.data['full_name']).exists():
            errors['full_name'] = 'This full name is already taken'


        if 'phone_num' in request.data and not re.match(r"^[0-9]{11}$", request.data['phone_num']):
            errors['phone_num'] = 'Invalid phone number format'
        if 'phone_num' in request.data and Admin.objects.filter(phone_num=request.data['phone_num']).exists():
            errors['phone_num'] = 'This phone number is already taken'

       

        return errors