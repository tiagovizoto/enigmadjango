from rest_framework import serializers
from job.models import Job, Candidaty
from django.contrib.auth.models import User

class CandidatySerializer(serializers.ModelSerializer):
    vaga_id = serializers.ReadOnlyField(source='job.id')

    name_job = serializers.ReadOnlyField(source='job.title')
    #allow_null = True
    #many = True
    class Meta:
        model = Candidaty
        fields = ('name', 'email', 'message', 'vaga_id', 'name_job')

class JobPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'created', 'modified', 'title', 'location', 'description')

class JobSerializer(serializers.ModelSerializer):
    rh = serializers.ReadOnlyField(source='rh.username')

    class Meta:
        model = Job
        fields = ('id', 'created', 'modified', 'title', 'location', 'description','rh')

class JobDetalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'created', 'modified', 'title', 'location', 'description')


class CandidatoVagaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidaty
        fields = ('id','name', 'email', 'message')


class UserSerializer(serializers.ModelSerializer):
    jobs = serializers.PrimaryKeyRelatedField(many=True, queryset=Job.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'jobs')