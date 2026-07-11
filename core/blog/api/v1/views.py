from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAdminUser ,IsAuthenticated
from .serializers import PostSerializer , CategorySerializer
from blog.models import Post , Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView , ListAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.generics import GenericAPIView , ListAPIView , ListCreateAPIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from .permission import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter
from .paginations import DefaultPagination
'''@api_view(["GET" , "POST"])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == "GET" :
        posts = Post.objects.filter(status= True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''

"""class PostList(APIView):
    '''getting a list of posts and creating a new post'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self,request):
        '''get a posts'''
        posts = Post.objects.filter(status= True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    def post(self,request):
        '''post a posts'''
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""

class PostList(ListCreateAPIView):
    '''getting a list of posts and creating a new post'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


'''@api_view(["GET" , "PUT" , "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request , id):
    post = get_object_or_404(Post , pk=id , status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail:item removed successfully"} , status=status.HTTP_204_NO_CONTENT)'''
    

"""class PostDetail(APIView):
    '''getting detail of the post and edit plus removing it '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    Serializer_class = PostSerializer
    def get(self,request,id):
        '''get post'''
        post = get_object_or_404(Post , pk=id , status=True)
        serializer = self.Serializer_class(post)
        return Response(serializer.data)
    def put(self,request,id):
        '''put post'''
        post = get_object_or_404(Post , pk=id , status=True)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,id):
        '''delete post'''
        post = get_object_or_404(Post , pk=id , status=True)
        post.delete()
        return Response({"detail:item removed successfully"} , status=status.HTTP_204_NO_CONTENT)"""


class PostDetail(RetrieveUpdateDestroyAPIView):
    '''getting detail of the post and edit plus removing it '''
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True) 

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend ,SearchFilter,OrderingFilter]
    filterset_fields = {'category':{"exact","in"}, 'author':{"exact"},'status':{"exact"}}
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination
class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()