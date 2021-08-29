from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# title
# status
# data-current
# user
# priority

class TODO(models.Model):
    Status_Choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING')]

    priority_Choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
    ]

    title = models.CharField(max_length=50)
    status = models.CharField(max_length=3, choices=Status_Choices)
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=3,choices=priority_Choices)
