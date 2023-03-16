from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers=models.ManyToManyField('auth.User', related_name='user_followers',blank=True)

class Post(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField('auth.User', related_name='likes', blank=True)

    class Meta:
        ordering = ('-created_at',)
    
    @property
    def comments(self):
        return Comment.objects.filter(post=self)
    
    @property
    def likes(self):
        return self.liked_by.all().count()

class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
