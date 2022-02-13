from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .views_helper import check_availability, encrypt_text
from .models import EncryptText
from encrypt.serializer import EncryptedFieldSerializer 


from .forms import EncryptTextField
# Create your views here.

class EncryptedTextCrud(APIView):

    def get(self, request):
        try:
            password = request.GET.get("password")
            password_digest = encrypt_text(password)
            et = EncryptText.objects.filter(
                password = password_digest
            ).first()

            return Response(
                data = {
                    "name" : et.name,
                },
                status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                data = None, 
                status = status.HTTP_500_INTERNAL_SERVER_ERROR,
                exception = e
            )

    def post(self, request):
        try:
            encrypted_text_form = EncryptTextField(request.data or None)

            if not encrypted_text_form.is_valid():
                return Response(
                    data = encrypted_text_form.errors,
                    status  = status.HTTP_400_BAD_REQUEST
                )

            cleaned_data = encrypted_text_form.cleaned_data
            # check if already password exist 
            check_availability(cleaned_data.get('password'))
            encrypted_details = encrypted_text_form.save()
            encrypted_details_serializer = EncryptedFieldSerializer(encrypted_details)
            return Response(
                    data = encrypted_details_serializer.data,
                    status  = status.HTTP_200_OK
                )
        except Exception as e:
            print(e)
            return Response(
                    data = str(e),
                    status  = status.HTTP_500_INTERNAL_SERVER_ERROR,
                    exception=e
                )

