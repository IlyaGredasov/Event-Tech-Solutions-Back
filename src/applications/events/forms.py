from .models import EventComment
from django.forms import ModelForm
class EventCommentForm(ModelForm):
    class Meta:
        model = EventComment
        fields = ('user', 'event', 'comment')