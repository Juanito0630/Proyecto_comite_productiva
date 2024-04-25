from rest_framework import serializers
from .models import Usuario, Proceso, PlanM, Comite,Iniciar, Generar, Cita

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('identificacion', 'nombre', 'direccion', 'telefono', 'correo', 'rol')

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = ('idProceso', 'fechaCitacion', 'descargos', 'decision', 'estado', 'justificacion', 'motivo', 'resumen', 'evidencias')

class PlanMSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanM
        fields = ('idPlanMejora', 'situacion', 'fechaInicio', 'fechaLimite', 'instructor')

class ComiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comite
        fields = ('idComite', 'fecha', 'hora', 'fechaActa', 'detallesActa')

class IniciarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iniciar
        fields = ('ficha', 'cedulaUsuario', 'idProceso')

class GenerarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generar
        fields = ('idProceso', 'idPlanM')

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ('idProceso', 'idComite')
