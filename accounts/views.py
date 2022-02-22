from accounts.models import User, Contest
from mainapp.serializers import (
                            UserProfileSerializer,
                            TokenSerializer,
                            ContestSerializer,
                            UserTokensSerializer)

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from mainapp.models import Token, UserTokens
from datetime import date
from accounts.serializers import AllUserSerializer

class UserModelViewSet(ModelViewSet):

    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    permission_classes = [IsAuthenticated, ]

    @action(methods=['get', ], detail=False)
    def my(self, request, *args, **kwargs):
        user = request.user
        username = user.username
        first_name = user.first_name
        last_name = user.last_name
        qr_quantity = user.qr_quantity
        qr_in_day = UserTokens.objects.filter(user=user, date=date.today()).count()
        which_contest = ContestSerializer(user.which_contest).data

        all_contest = Contest.objects.all().order_by('need_qr')
        contest_serializer = ContestSerializer(all_contest, many=True)
        #
        all_token = UserTokens.objects.filter(user=user)
        token_serializer = UserTokensSerializer(all_token, many=True)

        data = {

            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "qr_quantity": qr_quantity,
            "qr_in_day": qr_in_day,
            "which_contest": which_contest
        }
        return Response({
                    'profile': data,
                    'contests': contest_serializer.data,
            'tokens': token_serializer.data
                    })

    # 'tokens': token_serializer.data

class AllUsersView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AllUserSerializer
