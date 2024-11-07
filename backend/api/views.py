from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer, MovieSerializer, ChannelSerializer
from .models import Movie, Channel

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
    
class HomeViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def getInfoUser(self, request):
            # Kiểm tra xem người dùng có tồn tại hay không
        user = request.user
        if user.is_authenticated:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"error": "User not authenticated"}, status=401)
        
class MovieViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['GET'])
    def getMovieWhereGenre(self, request):
        idgenre = request.idgenre
        pass

    @action(detail=False, methods=['GET'])
    def getAllMovies(self, request):
        try:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": "Có lỗi xảy ra khi lấy danh sách phim"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['POST'])
    def addMovie(self, request):
        try:
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Thêm phim thành công",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                "error": "Dữ liệu không hợp lệ",
                "details": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "error": "Có lỗi xảy ra khi thêm phim",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChannelViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def addChannel(self, request):
        try:
            serializer = ChannelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Thêm kênh thành công",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                "error": "Dữ liệu không hợp lệ",
                "details": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "error": "Có lỗi xảy ra khi thêm kênh",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'])
    def getAllChannels(self, request):
        try:
            channels = Channel.objects.all()
            serializer = ChannelSerializer(channels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "Có lỗi xảy ra khi lấy danh sách kênh",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)