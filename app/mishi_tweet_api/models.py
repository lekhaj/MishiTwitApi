import random
from django.conf import settings
from django.db import models
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    permission_classes = (IsAuthenticated,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class TweetQuerySet(models.QuerySet):
    permission_classes = (IsAuthenticated,)
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_users_id = []
        if profiles_exist:
            followed_users_id = user.following.values_list("user__id", flat=True) # [x.user.id for x in profiles]
        return self.filter(
            Q(user__id__in=followed_users_id) |
            Q(user=user)
        ).distinct().order_by("-timestamp")

class TweetManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TweetQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)

class Tweet(models.Model):
    permission_classes = (IsAuthenticated,)
    # Maps to SQL data
    # id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets") # many users can many tweets
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TweetManager()
    # def __str__(self):
    #     return self.content
    
    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    
    def serialize(self):
        '''
        Feel free to delete!
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }

class FollowerRelation(models.Model):
    permission_classes = (IsAuthenticated,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    permission_classes = (IsAuthenticated,)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    """
    project_obj = Profile.objects.first()
    project_obj.followers.all() -> All users following this profile
    user.following.all() -> All user profiles I follow
    """