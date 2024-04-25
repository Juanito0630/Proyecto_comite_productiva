from .models import Usuario, Proceso, PlanM, Comite, Iniciar, Generar, Cita
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer, ProcesoSerializer, PlanMSerializer, ComiteSerializer, IniciarSerializer, GenerarSerializer, CitaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProcesoSerializer

class PlanMViewSet(viewsets.ModelViewSet):
    queryset = PlanM.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlanMSerializer

class ComiteViewSet(viewsets.ModelViewSet):
    queryset = Comite.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ComiteSerializer

class IniciarViewSet(viewsets.ModelViewSet):
    queryset = Iniciar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IniciarSerializer

class GenerarViewSet(viewsets.ModelViewSet):
    queryset = Generar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GenerarSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CitaSerializer