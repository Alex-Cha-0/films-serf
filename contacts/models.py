from django.contrib.auth.models import User
from django.db import models
from django.db.models import JSONField


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    film_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    createdDate = models.DateTimeField(auto_now_add=True)
    j_field = JSONField()
    post_like = models.SmallIntegerField(default=0)
    userWhoLikes = models.ManyToManyField(User, through='UserPostRelation', related_name='posts')

    def postLike(self):
        self.post_like += 1
        self.save()

    def postDislike(self):
        self.post_like -= 1
        self.save()

    def __str__(self):
        return f"{self.film_id}"


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    submit = models.BooleanField()

    def __str__(self):
        return self.commentUser.email

    class Meta:
        ordering = ('-createdDate',)


class UserPostRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}: {self.post}'

