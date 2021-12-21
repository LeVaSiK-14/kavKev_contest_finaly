from rest_framework.serializers import ModelSerializer, ReadOnlyField
from mainapp.models import Token, UserTokens
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
    class Meta:
        model = Token
        fields = ['id', 'token', 'slug', 'isActive']
        read_only_fields = ['isActive', ]


class ContestSerializer(ModelSerializer):
    class Meta:
        model = Contest
        fields = ['id', 'need_qr', 'name_contest', 'image', 'amount_prize', 'is_main']

class UserTokensSerializer(ModelSerializer):
    token = ReadOnlyField(source='token.token')
    user = ReadOnlyField(source='user.username')
    class Meta:
        model = UserTokens
        fields = ['id', 'user', 'token', 'date']

