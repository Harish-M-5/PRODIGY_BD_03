from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response([u.to_json() for u in users])

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        if not name or not email:
            return Response({"error": "Name and Email required"}, status=400)
        user = User(name=name, email=email)
        user.save()
        return Response(user.to_json(), status=201)

class UserDetail(APIView):
    def get(self, request, id):
        user = User.objects(id=id).first()
        if not user:
            return Response({"error": "User not found"}, status=404)
        return Response(user.to_json())

    def put(self, request, id):
        user = User.objects(id=id).first()
        if not user:
            return Response({"error": "User not found"}, status=404)
        user.name = request.data.get('name', user.name)
        user.email = request.data.get('email', user.email)
        user.save()
        return Response(user.to_json())

    def delete(self, request, id):
        user = User.objects(id=id).first()
        if not user:
            return Response({"error": "User not found"}, status=404)
        user.delete()
        return Response(status=204)
