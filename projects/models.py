from django.db import models

# Create your models here.
class Usuario(models.Model):
    identificacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    rol = models.CharField(max_length=50)



class Proceso(models.Model):
    idProceso = models.AutoField(primary_key=True)
    fechaCitacion = models.DateField()
    descargos = models.TextField()
    decision = models.TextField()
    estado = models.CharField(max_length=50)
    justificacion = models.TextField()
    motivo = models.TextField()
    resumen = models.TextField()
    evidencias = models.TextField()

class PlanM(models.Model):
    idPlanMejora = models.AutoField(primary_key=True)
    situacion = models.TextField()
    fechaInicio = models.DateField()
    fechaLimite = models.DateField()
    instructor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Comite(models.Model):
    idComite = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateTimeField()
    fechaActa = models.DateField()
    detallesActa = models.TextField()

class Iniciar(models.Model):
    ficha = models.IntegerField()
    cedulaUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)

class Generar(models.Model):
    idProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    idPlanM = models.ForeignKey(PlanM, on_delete=models.CASCADE)

class Cita(models.Model):
    idProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    idComite = models.ForeignKey(Comite, on_delete=models.CASCADE)
