# -*- coding: utf-8 -*-
import json

from django.utils.encoding import smart_text
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication, get_authorization_header


class FakeUser(object):
    def __init__(self, id, username):
        self.pk = id
        self.id = id
        self.username = username

    def is_authenticated(self):
        return True


class JSONAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = smart_text(get_authorization_header(request))
        # if user is not authenticated, auth_header is empty
        if not auth_header:
            raise AuthenticationFailed()
        try:
            user_data = json.loads(auth_header)
        except:
            raise AuthenticationFailed()

        return FakeUser(user_data.get('id'), user_data.get('username')), "JSONAuth"