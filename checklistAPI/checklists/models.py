from django.db import models
from django.contrib.auth.models import User

class ChecklistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checklists')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def is_root(self):
        return self.parent is None
