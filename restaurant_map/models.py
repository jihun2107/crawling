from django.db import models


# Create your models here.
# models.py
class Restaurant(models.Model):
    restaurant_id = models.AutoField(db_column='restaurant_ID', primary_key=True)  # Field name made lowercase.
    restaurant_name = models.CharField(max_length=255)
    restaurant_address = models.CharField(max_length=255, blank=True, null=True)
    restaurant_latitude = models.CharField(max_length=255, blank=True, null=True)
    restaurant_longitude = models.CharField(max_length=255, blank=True, null=True)
    review_crawling_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurants'


class Review(models.Model):
    review_id = models.AutoField(db_column='review_ID', primary_key=True)  # Field name made lowercase.
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING,
                                   db_column='restaurant_ID')  # Field name made lowercase.
    review_title = models.CharField(max_length=2048)
    review_link = models.TextField()
    review_description = models.TextField()
    blog_crawling_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Blog(models.Model):
    blog_id = models.AutoField(db_column='blog_ID', primary_key=True)  # Field name made lowercase.
    review = models.ForeignKey(Review, models.DO_NOTHING, db_column='review_ID')  # Field name made lowercase.
    blog_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'blogs'


