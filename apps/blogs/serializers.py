from rest_framework import serializers
from .models import Post,Like

# like serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

# post serializer
class PostSerializer(serializers.ModelSerializer):
    liked_by = LikeSerializer(many=True, read_only=True, source='blog_post')
    liked_count = serializers.SerializerMethodField()
    
    def get_liked_count(self,post):
        return Like.objects.filter(post_id=post.id).count()

    class Meta:
        model = Post
        fields = ["user", "title", "description", "content", "liked_by", "liked_count"]
        
        
        
