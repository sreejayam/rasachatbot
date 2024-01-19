



from django.db import models
from django.conf import settings

class ChatMessage(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show_buttons = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.timestamp}: {self.content}'
