from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Contact model for storing user contact information
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.IntegerField()
    contact_message = models.TextField()
    time_stamp = models.DateField(auto_now_add=True, blank=True)


# UserProfile model for storing user profile details
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    profile_picture = CloudinaryField(
        'image', folder='profile_picture', blank=True, null=True
    )

    def __str__(self):
        return self.user.username


# Destination model to store information about travel destinations
class Destination(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    SEASON_CHOICES = [
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn'),
        ('Winter', 'Winter')
    ]
    best_time_to_visit = models.CharField(
        max_length=6, choices=SEASON_CHOICES, default='Spring'
    )

    BUDGET_CHOICES = [
        ('Budget', 'Budget'),
        ('Mid-range', 'Mid-range'),
        ('Luxury', 'Luxury')
    ]
    budget_type = models.CharField(
        max_length=10, choices=BUDGET_CHOICES, default='Mid-range'
    )

    image = CloudinaryField(
        'image', folder='destinations', blank=True, null=True
    )
    is_favorite = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='destinations', default=1
    )
    favorites = models.ManyToManyField(
        User, related_name='favorite_destinations', blank=True
    )
    likes = models.ManyToManyField(
        User, related_name='liked_destinations', blank=True
    )

    def __str__(self):
        return self.name

    def total_likes(self):
        return self.likes.count()
