from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class LikeView(views.APIView):
    # serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Post, pk=kwargs["post_id"])
        user = self.request.user
        if request.data["like"] == "True":
            if user in obj.dislikes.all():
                obj.dislikes.remove(user)
                obj.likes.add(user)
            elif user in obj.likes.all():
                pass
            else:
                obj.likes.add(user)
        elif request.data["like"] == "False":
            if user in obj.likes.all():
                obj.dislikes.add(user)
                obj.likes.remove(user)
            elif user in obj.dislikes.all():
                pass
            else:
                obj.dislikes.add(user)
        else:
            Response(status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
