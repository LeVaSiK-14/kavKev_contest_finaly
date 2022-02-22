from rest_framework.serializers import ModelSerializer
from accounts.models import User

class AllUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name','last_name', 'which_contest']
