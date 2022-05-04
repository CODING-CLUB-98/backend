from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from user.models import User

from .serializers import ClassSerializer
from .models import Class
from .permissions import HasPermission, HasOwnerPermission


from base.models import Subject, Department, Semester, Batch


class ClassList(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request):
        try:
            classes = []
            if request.user.user_type == User.UserType.STUDENT:
                classes = request.user.student.classes.all()
            elif request.user.user_type == User.UserType.TEACHER:
                classes = request.user.teacher.classes.all()
            else:
                return Response('user does not have classes', status=status.HTTP_404_NOT_FOUND)
            serializer = ClassSerializer(classes, many=True)
            return Response(serializer.data)
        except(Class.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class ClassDetail(APIView):
    permission_classes = [IsAuthenticated & HasOwnerPermission]

    def get(self, request, id):
        try:
            c = Class.objects.get(pk=id)
            serializer = ClassSerializer(c)
            return Response(serializer.data)
        except(Class.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        try:
            serializer = ClassSerializer(data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(IntegrityError):
            return Response('class not unique', status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            c = Class.objects.get(pk=id)
            self.check_object_permissions(request, c)
            serializer = ClassSerializer(c, data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(IntegrityError):
            return Response('class not unique', status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            c = Class.objects.get(pk=id)
            self.check_object_permissions(request, c)
            c.delete()
            return Response('deleted', status=status.HTTP_200_OK)
        except(IntegrityError):
            return Response('class not unique', status=status.HTTP_400_BAD_REQUEST)
