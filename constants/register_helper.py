from django.contrib.auth.models import User

class RegisterHelper():
    def validate_data(request):
        errors = {}
        ############## Check Fields if Empty ################
        if 'first_name' in request.data and request.data['first_name'] == '':
            errors['first_name'] =  'First name should not be empty'

        if 'last_name' in request.data and request.data['last_name'] == '':
            errors['last_name'] =  'Last name should not be empty'

        if 'birthday' in request.data and request.data['birthday'] == '':
            errors['birthday'] =  'Birthday should not be empty'
        
        if 'gender' in request.data and request.data['gender'] == '':
            errors['gender'] =  'Gender should not be empty'
        
        if 'email' in request.data and request.data['email'] == '':
            errors['email'] =  'Email should not be empty'

        if 'phone_number' in request.data and request.data['phone_number'] == '':
            errors['phone_number'] =  'Phone number should not be empty'

        if 'password' in request.data and request.data['password'] == '':
            errors['password'] =  'Password should not be empty'

        ############## Check if Existing ####################
        if request.data['first_name'] and User.objects.filter(username=request.data["first_name"]).count() != 0:
            errors['first_name'] = 'First name is already used'

        if request.data['email'] and User.objects.filter(email=request.data["email"]).count() != 0:
            errors['email'] = 'Email has already been used'

        ############## Validate Fields ######################
        if request.data['password'] != request.data['confirm_password']:
            errors['password'] = 'Password does not match'

        if len(request.data['phone_num']) != 11:
            errors['phone_number'] = 'Please Enter a valid phone number'

        if request.data['phone_num'][:2] != '09':
            errors['phone_number'] = 'Please Enter Philippine-based mobile number'

        return errors
    
    # def validate_image(self,request):
    #     errors = {}
        
    #     if 'signature' in request.data:
    #         if request.data['signature'] != '':
    #             signature_size = request.data['signature'].size
    #             signature_ext = request.FILES["signature"]
                
    #             if float(signature_size) > 5000000:
    #                 errors['signature_size'] = "You cannot upload file more than 5Mb"

    #             if signature_ext.content_type != 'image/png' and signature_ext.content_type != 'image/jpeg':
    #                 errors['signature_ext'] = "Only use .PNG files or .JPEG files"

    #     if 'profile_picture' in request.data:
    #         if request.data['profile_picture'] != '':
    #             profile_picture_size = request.data['profile_picture'].size
    #             profile_picture_ext = request.FILES["profile_picture"]

    #             if float(profile_picture_size) > 5000000:
    #                 errors['profile_size'] = "You cannot upload file more than 5Mb"
                    
    #             if profile_picture_ext.content_type != 'image/png' and profile_picture_ext.content_type != 'image/jpeg':
    #                 errors['profile_ext'] = "Only use .PNG files or .JPEG files"
            
    #     self.errors = errors

    #     return self.errors