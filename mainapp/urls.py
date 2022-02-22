from django.urls import path
from mainapp.views import ListCreateToken, RetrieveUpdateToken
from accounts.views import UserModelViewSet, AllUsersView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('profile', UserModelViewSet)
router.register('all_users', AllUsersView)

urlpatterns = [
    path('token/', ListCreateToken.as_view()),
    path('token/<slug:slug>/', RetrieveUpdateToken.as_view()),
]

urlpatterns += router.urls
