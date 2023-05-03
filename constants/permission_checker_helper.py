class PermissionChecker():
    def validate_permission_edit(self,payload): ### Admin and Super Admin ###
        errors = {}

        if 'position_level' not in payload:
            errors['position_level'] = 'Some User Credentials is missing' 

        if payload['position_level'] == 'S':
            errors['position_level'] = 'You are not permitted to update'
        
        return errors

    def validate_permission_add_user(self,payload): ### Super Admin ###
        errors = {}

        if 'position_level' not in payload:
            errors['position_level'] = 'Some User Credentials is missing' 

        if payload['position_level'] == 'S' or payload['position_level'] == 'A':
            errors['position_level'] = 'You are not permitted to add new users'
        
        return errors

    def validate_permission_delete(self,payload): ### Admin and Super Admin ###
        errors = {}

        if 'position_level' not in payload:
            errors['position_level'] = 'Some User Credentials is missing' 

        if payload['position_level'] == 'S':
            errors['position_level'] = 'You are not permitted to delete'
        return errors
    
    def validate_permission_control(self,payload): ### Admin and Super Admin ###
        errors = {}

        if 'position_level' not in payload:
            errors['position_level'] = 'Some User Credentials is missing' 

        if payload['position_level'] != 'SA':
            errors['position_level'] = 'Only Super Admin can edit User Permission'        
        
        return errors
    
