from rest_framework.viewsets import ModelViewSet
from user_app.models import User
from user_app.api.serializers import UserSerializer



class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('__all__')
