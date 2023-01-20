from django.db import models
import torch


class ChatGPT(models.Model):
    input_text = models.CharField(max_length=100)
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
