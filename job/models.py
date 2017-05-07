from django.db import models


# Create your models here.


class Job(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    location = models.CharField(max_length=100)
    # expiration = models.DateTimeField()
    description = models.TextField()
    rh = models.ForeignKey('auth.User', related_name='job', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['created']

    def __str__(self):
        return self.title


class Candidaty(models.Model):

    name = models.CharField(max_length=140)
    email = models.CharField(max_length=222)
    message = models.CharField(max_length=222)
    job = models.ForeignKey('job.Job',verbose_name='Vaga')
    join_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Candidato'
        ordering=['join_date']

    def __str__(self):
        return self.name


