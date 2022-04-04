from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Post, Group


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthorOrReadOnly,
        IsAuthenticated,
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthorOrReadOnly,
        IsAuthenticated,
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(
            author=self.request.user,
            post=post
        )
