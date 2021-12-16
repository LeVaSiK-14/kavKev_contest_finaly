from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as django_filter
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from mainapp.models import Token
from mainapp.serializers import TokenSerializer, ContestSerializer
from accounts.models import Contest
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST





class ListCreateToken(ListCreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    # permission_classes = [IsAdminUser, ]
    filter_backends = [django_filter.DjangoFilterBackend, SearchFilter]
    filter_fields = ['token', ]
    search_fields = ['token', ]
    


class RetrieveUpdateToken(RetrieveUpdateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    lookup_field = 'slug'


    def update(self, request, *args, **kwargs):
        token = self.get_object()
        user = request.user
        if token.isActive == False:
            return Response({'Error': 'Данный QR код был отсканирован ранее'}, status=HTTP_404_NOT_FOUND)
        else:
            if user.qr_in_day >= 3:
                return Response({'Error': 'В день можно отсканировать не более 3 QR кодов'}, status=HTTP_400_BAD_REQUEST)
            else:

                token.user = user
                token.isActive = False
                token.save()
                user.qr_quantity += 1
                user.qr_in_day += 1
                user.save()

                contests = Contest.objects.all().order_by('need_qr')
                if user.qr_quantity < contests.first().need_qr:
                    return Response({
                                    "Success": 
                                    f"Отсканируйте больше {contests.first().need_qr} Qr кодов, что бы начать учавствовать в конкурсе! {contests.first().name_contest}"})
                elif user.qr_quantity >= contests.last().need_qr:
                    user.which_contest = contests.last()
                    user.save()
                    return Response({"Success": f"Поздравляем вы учавствуете в самом большом конкурсе на !{contests.last().name_contest}"})
                else:
                    for i in range(1, len(contests)):
                        if user.qr_quantity >= contests[i-1].need_qr and user.qr_quantity < contests[i].need_qr:
                            user.which_contest = contests[i-1]
                            user.save()
                            return Response({"Success": f"Поздравляем вы учавствуете в конкурсе на {contests[i-1].name_contest}!"})