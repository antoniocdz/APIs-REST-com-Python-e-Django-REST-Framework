from rest_framework.views import APIView
from rest_framework.response import  Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import status

class CursoAPIView(APIView):
    """
    API de Cursos
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serilizer = CursoSerializer(cursos, many=True)
        return Response(serilizer.data)

    def post(self, request):
        serilizer = CursoSerializer(data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.data, status=status.HTTP_201_CREATED)
        #return Response({"msg": "Criou com sucesso!"}, status=status.HTTP_201_CREATED)
        #return Response({"id": serilizer.data['id'], "curso": serilizer.data['titulo']}, status=status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):
    """
    API de Avaliações
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serilizer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serilizer.data)

    def post(self, request):
        serilizer = AvaliacaoSerializer(data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.data, status=status.HTTP_201_CREATED)
        # return Response({"msg": "Criou com sucesso!"}, status=status.HTTP_201_CREATED)
        # return Response({"id": serilizer.data['id'], "avaliação": serilizer.data['curso']}, status=status.HTTP_201_CREATED)