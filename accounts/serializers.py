# -*- coding: utf-8 -*-
__author__ = "Tiago Vizoto"
__email__ = "vizoto123@gmail.com"

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'job')