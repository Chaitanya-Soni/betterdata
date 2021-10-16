from django.db import models
# Create your models here.
from django.core.validators import RegexValidator
from .validators import validate_file_extension
def increment_project_number():
  total = len(project.objects.all())
  return "Project-"+str(total+1)
def increment_model_number():
  total = len(project.objects.all())
  return "Model-"+str(total+1)

class project(models.Model):
    proj = models.CharField(max_length = 20, default = increment_project_number)
    def __str__(self):
        return self.proj

    class Meta:
        order_with_respect_to = 'proj'
class realdata(models.Model):
    proj = models.ForeignKey(project, on_delete=models.CASCADE,null=True)
    real_data = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension],blank=True)
    name = models.CharField(max_length = 20)
    def __str__(self):
        name = str(self.real_data).split('/')
        print(name)
        return name[-1]

    class Meta:
        order_with_respect_to = 'real_data'
class modelData(models.Model):
    proj = models.ForeignKey(project, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.name)

    class Meta:
        order_with_respect_to = 'name'
class parameters (models.Model):
    name=models.OneToOneField(modelData ,  on_delete=models.CASCADE, null=True, blank=True)
    batch_size=models.IntegerField()
    training_cycles=models.IntegerField()
    def __str__(self):
        return str(self.name)

class syntheticdata (models.Model):
    name=models.ForeignKey(modelData ,  on_delete=models.CASCADE, null=True, blank=True)
    synthetic_data = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension],blank=True)
    def __str__(self):
        n = str(self.synthetic_data).split('/')
        return n[-1]

    class Meta:
        order_with_respect_to = 'name'