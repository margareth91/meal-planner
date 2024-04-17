from rest_framework import generics, status
from rest_framework.response import Response

from accounts.serializers import UserSignUpSerializer


class UserSignUpView(generics.GenericAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "User created successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
