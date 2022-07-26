from django.db import models

# Step 1: Name the model and inherit from the django Model class
class City(models.Model):
    # Step 2: Add any fields on the erd
    name = models.CharField(max_length=155)
