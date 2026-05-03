from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderer import TemplateHTMLRenderer, JSONRenderer
from django.shortcuts import redirect

from .selectors import  get_user_all,get_user_by_id
from .serializers import UserSerializer
from services import create_user,user_delete,user_update
class UserListCreateAPIView(APIView):
    renderer_classes=[TemplateHTMLRenderer, JSONRenderer]
    template_name=''
    

    def get(self,request,pk):
        users=get_user_all()
        if request.accepted_renderer.format=="json":
            serializer=UserSerializer(users,many=True)
            return Response({'users':users})
        

    def post (self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            create_user(**serializer.validated_data)
            if request.accepted_renderer.format=='jason':
                return Response({"msg":"Success"}, status=201)
            return redirect('user-list')
        return Response(serializer.errors,status=400)
    
class UserDetailAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'accounts/user_detail.html'

    def get(self, request, pk):
        user = get_user_by_id(pk)
        if request.accepted_renderer.format == 'json':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({'user': user})
    
    def post(self, request, pk): # HTML Form Update
        serializer = UserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            user_update(user_id=pk, **serializer.validated_data)
            return redirect('user-list')
        return Response(serializer.errors, status=400)