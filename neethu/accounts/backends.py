from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailOrUserName(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        try:
            # Try to get the user by username or email
            user = UserModel.objects.get(Q(username=username) | Q(email=username))
        except UserModel.DoesNotExist:
            return None
        except UserModel.MultipleObjectsReturned:
            # Handle the case where multiple users are returned
            # This might happen if both username and email are not unique.
            return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        return None
