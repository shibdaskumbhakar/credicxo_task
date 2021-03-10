from django.shortcuts import render
from .serializers import UserSerializer
# Create your views here.


from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from rest_framework import generics
from .permissions import IsTeacher, IsStudent
from django.contrib.auth.hashers import make_password


################# Signup FOr Teacher And Student ##################
# for create 3 level user i use django groups, groups name are teacher,student and admin
class SignupForStudentOrTeacher(APIView):
    def post(self, request, format=None):
        seralizer = UserSerializer(data=request.data)
        if seralizer.is_valid():
            user_type = request.data['user_type']
            email = request.data['email']
            username = request.data['username']
            password = make_password(self.request.data['password'])
            if user_type == 'student':
                seralizer.save(password=password)
                user = User.objects.get(
                    email=email, username=username)
                group = Group.objects.get(name="student")
                group.user_set.add(user)
                return Response({'mesg': 'New Student Add Succesful'})
            elif user_type == 'teacher':
                seralizer.save(password=password)
                user = User.objects.get(
                    email=email, username=username)
                group = Group.objects.get(name="teacher")
                group.user_set.add(user)
                return Response({'mesg': 'New Teacher Add Succesful'})
            else:
                return Response({'mesg': 'plese add user type teacher or student'})
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)


# This api for Login Student Detalis
############# If STUDENT is login then student get his informations ###############
class StudentDetailsView(APIView):
    # use custom permission for Student
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request, format=None):
        if request.user.groups.filter(name='student').exists():
            user = User.objects.get(username=request.user.username)
            return Response({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'messg': 'student group',
            })
        else:
            return Response({
                'messg': 'not student',
            })

########## view for admin add/list ###########
########## Admin has permission to add student and teacher  ###########


class AdminUserView(APIView):
    permission_classes = [permissions.IsAdminUser, IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.all()
        seralizer = UserSerializer(user, many=True)
        return Response(seralizer.data)

    def post(self, request, format=None):
        seralizer = UserSerializer(data=request.data)
        if seralizer.is_valid():
            user_type = request.data['user_type']
            email = request.data['email']
            username = request.data['username']
            password = make_password(self.request.data['password'])
            if user_type == 'student':
                seralizer.save(password=password)
                user = User.objects.get(
                    email=email, username=username)
                group = Group.objects.get(name="student")
                group.user_set.add(user)
                return Response({'mesg': 'New Student Add Succesful'})
            elif user_type == 'teacher':
                seralizer.save(password=password)
                user = User.objects.get(
                    email=email, username=username)
                group = Group.objects.get(name="teacher")
                group.user_set.add(user)
                return Response({'mesg': 'New Teacher Add Succesful'})
            else:
                return Response({'mesg': 'plese add user type teacher or student'})
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)


############### Teacher has permission to add student and list all the student ###############

class TeacherActionAddListView(APIView):
    # use custom permission for teacher
    permission_classes = [IsTeacher, IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.filter(groups__name='student')
        seralizer = UserSerializer(user, many=True)
        return Response(seralizer.data)

    def post(self, request, format=None):
        seralizer = UserSerializer(data=request.data)
        if seralizer.is_valid():
            user_type = request.data['user_type']
            email = request.data['email']
            username = request.data['username']
            password = make_password(self.request.data['password'])

            if user_type == 'student':
                seralizer.save(password=password)
                user = User.objects.get(
                    email=email, username=username)
                group = Group.objects.get(name="student")
                group.user_set.add(user)
                return Response({'mesg': 'New Student Add Succesful'})
            else:
                return Response({'mesg': 'plese add user_type  student'})
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
