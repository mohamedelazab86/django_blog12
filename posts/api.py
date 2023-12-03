# functions
from .models import Post
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


@api_view(['GET'])
def list_api(request):
    posts=Post.objects.all()
    data=PostSerializer(posts,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def detail_api(request,pk):
    post=Post.objects.get(id=pk)
    data=PostSerializer(post).data
    return Response({'data':data})



from rest_framework import generics
class List_Api(generics.ListAPIView):
    queryset =Post.objects.all()
    serializer_class=PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'draft']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['publish_date']

class Detail_APi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
  
    
    
