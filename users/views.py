from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from users.serializers import RegisterSerializer, UserSerializer


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user':
                UserSerializer(
                    user,
                    context=self.get_serializer_context()
                ).data,
            'message':
                'User created successfully. Now perform Login to get your token'
        })
