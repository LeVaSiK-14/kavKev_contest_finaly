from rest_framework.serializers import ModelSerializer, ReadOnlyField
from mainapp.models import Token
from accounts.models import Contest, User

class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
        ]


class TokenSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.first_name')
    class Meta:
        model = Token
        fields = ['id', 'token', 'slug', 'isActive', 'user']
        read_only_fields = ['isActive', ]


class ContestSerializer(ModelSerializer):
    class Meta:
        model = Contest
        fields = ['id', 'need_qr', 'name_contest', 'image', 'amount_prize', 'is_main']
