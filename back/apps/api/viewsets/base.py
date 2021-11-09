from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class BaseViewSet(ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = None
    model_class = None

    def get_queryset(self, **kwargs):
        queryset = self.model_class.objects.all()

        if "pk" in kwargs:
            queryset = queryset.filter(id=kwargs.get('pk'))

        return queryset

    def list(self, request, *args, **kwargs):
        try:
            data = request.GET.copy()
            queryset = self.get_queryset(**data.dict())
            serializer = self.serializer_class(queryset, many=True)

            return Response({
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'An error has ocurred',
                'err': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)
            if not pk:
                return Response({
                    'message': 'Id is required'
                }, status=status.HTTP_400_BAD_REQUEST)

            queryset = self.get_queryset(pk=pk).first()
            if not queryset:
                return Response({
                    'message': 'Item not found'
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.serializer_class(queryset)

            return Response({
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'An error has ocurred',
                'err': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            return Response({
                'message': 'Create method'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'An error has ocurred',
                'err': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)
            if not pk:
                return Response({
                    'message': 'Update method'
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'message': 'Update'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'An error has ocurred',
                'err': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)
            if not pk:
                return Response({
                    'message': 'Id is required'
                }, status=status.HTTP_400_BAD_REQUEST)

            queryset = self.get_queryset(pk=pk)
            if not queryset:
                return Response({
                    'message': 'Item not found'
                }, status=status.HTTP_404_NOT_FOUND)

            queryset.delete()

            return Response({
                'message': 'Item has been removed'
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                'message': 'An error has ocurred',
                'err': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
