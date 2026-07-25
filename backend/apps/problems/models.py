from django.db import models

class Problem(models.Model):
    DIFFICULTY_CHOICES = [('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    description = models.TextField()
    constraints = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='testcases')
    input = models.TextField()
    expected_output = models.TextField()
    is_sample = models.BooleanField(default=False)
    weight = models.IntegerField(default=1)
