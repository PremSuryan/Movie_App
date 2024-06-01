from django.db import models

# Create your models here.
class insert_movie(models.Model):

    title = models.CharField(max_length=100)
    blog_date = models.DateField()
    poster = models.ImageField(upload_to='movie')
    release_date = models.DateField()
    story = models.TextField()
    review = models.TextField()
    movie_rating = models.DecimalField(max_digits = 5,decimal_places=1)
    def __str__(self):
        return self.title
    
class comments(models.Model):
    username = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateField(auto_now=True)
    user_rating = models.DecimalField(max_digits=10,decimal_places=1)
    review = models.ForeignKey(insert_movie,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment




