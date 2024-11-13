import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moja_strona.settings')
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def create_tokens_for_users():
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)


if __name__ == "__main__":
    create_tokens_for_users()
