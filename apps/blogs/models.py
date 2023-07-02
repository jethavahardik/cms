from django.db import models
from apps.account.models import User
from  apps.account.models import TimeStampModel

# post model
class Post(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField()

# like model
class Like(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="liked_by")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="blog_post")

