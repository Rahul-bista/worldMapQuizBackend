from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from guessTheFlag.models import GuessTheFlag


# Serializer class
class Serializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = GuessTheFlag

# Create your views here.
class GuessTheFlagView(APIView):
    serializer_class = Serializer
    def get(self, request):
        model = GuessTheFlag.objects.all()
        serializer = self.serializer_class(model, many=True)
        return Response(serializer.data)