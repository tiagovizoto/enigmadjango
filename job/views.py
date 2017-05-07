
from .models import Job,Candidaty
from django.contrib.auth.models import User

from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from job.serializers import JobSerializer, CandidatySerializer, JobDetalSerializer,CandidatoVagaSerializer,UserSerializer,JobPublicSerializer

# Create your views here.

class JobListPublic(APIView):

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobPublicSerializer(jobs)
        return JsonResponse(serializer.data, safe=False)

class JobList(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return JsonResponse(serializer.data, safe=False)



class JobDetailPublic(APIView):

    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        job = self.get_object(pk)
        serializer = JobDetalSerializer(job)
        return JsonResponse(serializer.data, safe=False)


class JobDetail(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        job = self.get_object(pk)
        serializer = JobDetalSerializer(job)
        can = Candidaty.objects.filter(job=job.id)
        can = CandidatoVagaSerializer(can, many = True)
        return JsonResponse({'vaga' : serializer.data, 'candidaty': can.data}, safe=False)

    def put(self, request):
        data = JSONParser().parse(request)
        serializer = JobSerializer(self.get_object(pk), data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        job = self.get_object()
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def perform_create(self, serializer):
        serializer.save(rh=self.request.user)


class CandidatyList(APIView):

    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)

    def get(self, request):
        candidato = Candidaty.objects.all()
        serializer = CandidatySerializer(candidato, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

class CandidatyApplyJob(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CandidatySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer