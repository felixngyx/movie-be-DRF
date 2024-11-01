from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

class AuthViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def test_token(self, request):
        return Response({'message': 'Token is valid'})
    
class HomeViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
    # Nếu bạn cần thêm các method khác:
    def retrieve(self, request, pk=None):
        return Response({'message': f'Hello, {pk}!'})

    def create(self, request):
        return Response({'message': 'Created!'})

    def update(self, request, pk=None):
        return Response({'message': f'Updated {pk}!'})

    def partial_update(self, request, pk=None):
        return Response({'message': f'Partially updated {pk}!'})

    def destroy(self, request, pk=None):
        return Response({'message': f'Deleted {pk}!'})

    # Custom actions
    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        return Response({'message': 'Custom action!'})

    @action(detail=True, methods=['post'])
    def custom_detail_action(self, request, pk=None):
        return Response({'message': f'Custom action for {pk}!'})