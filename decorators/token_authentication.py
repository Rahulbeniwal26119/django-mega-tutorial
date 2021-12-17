from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from decorators.models import AuthToken, Faculty

class FaculatyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            raise AuthenticationFailed("Token not provided")
        
        try:
            token_id = token.split(' ')[1]
        except :
            raise AuthenticationFailed("Invalid token format")
        
        try:
            faculty_pk = AuthToken.objects.get(key=token_id).user.id 
            faculty = Faculty.objects.get(id=faculty_pk)
        except AuthToken.DoesNotExist:
            raise AuthenticationFailed("Invalid token")
        except Faculty.DoesNotExist:
            raise AuthenticationFailed("No faculy found")
        return (faculty, token_id)