from django.db import models
from accounts.models import User


class Token(models.Model):
    token = models.CharField(max_length=127, default='')
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(max_length=127, default='')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.token

class UserTokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    token = models.ForeignKey(Token, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.token.token}'