
from django import forms 
from .models import Article, Topic, Comment

class InputForm(forms.Form):
     name = forms.CharField()
     email = forms.EmailField()

class TopicForm(forms.ModelForm):
     
     class Meta():
          model = Topic
          fields = ('topic_name',)
          
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['topic', 'title', 'article', 'image']
        widgets = {
            'topic': forms.Select(), 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].queryset = Topic.objects.all()
          
class MyForm(forms.Form):
    name = forms.CharField(max_length=300)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # This should be the model class, not a string
        fields = ['name', 'body'] 
    