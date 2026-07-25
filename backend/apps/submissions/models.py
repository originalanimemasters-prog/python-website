from django.db import models

class Submission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('accepted', 'Accepted'),
        ('wrong_answer', 'Wrong Answer'),
        ('time_limit_exceeded', 'Time Limit Exceeded'),
        ('runtime_error', 'Runtime Error'),
    ]
    
    LANGUAGE_CHOICES = [('python', 'Python'), ('javascript', 'JavaScript'), ('java', 'Java'), ('cpp', 'C++')]
    
    problem = models.ForeignKey('problems.Problem', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    source_code = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    runtime_ms = models.IntegerField(null=True, blank=True)
    memory_kb = models.IntegerField(null=True, blank=True)
    output = models.TextField(blank=True)
    error_message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
