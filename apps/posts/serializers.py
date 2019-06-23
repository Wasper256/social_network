from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'created', 'likes',
                  'dislikes')

    @staticmethod
    def get_likes(obj):
        return obj.likes.count()

    @staticmethod
    def get_dislikes(obj):
        return obj.likes.count()


# class PostCreateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'content', 'author', 'created')