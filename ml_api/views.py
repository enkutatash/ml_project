from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .ml_model import models
from .serializers import PredictionNamedSerializer
import traceback

class PredictView(APIView):
    def post(self, request):
        try:
            serializer = PredictionNamedSerializer(data=request.data)
            if serializer.is_valid():
                model_name = serializer.validated_data['model']
                features = serializer.get_feature_array()
                model = models[model_name]
                prediction = model.predict([features])
                return Response({
                    'model_used': model_name,
                    'score': float(prediction[0])
                })
            else:
                return Response({'error': 'Validation failed', 'details': serializer.errors})
        except Exception as e:
            tb = traceback.format_exc()
            return Response({'error': str(e), 'traceback': tb}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
