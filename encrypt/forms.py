from django.forms import ModelForm
from .models import EncryptText
from .views_helper import encrypt_text

class EncryptTextField(ModelForm):

    class Meta:
        model = EncryptText
        fields = '__all__'

    def clean(self):
        password = self.cleaned_data.get('password')
        digest = encrypt_text(password)
        self.cleaned_data["password"] = digest 
        print(self.cleaned_data)
        super(EncryptTextField, self).clean()
