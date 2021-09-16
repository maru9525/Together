# from django import forms
# from .models import Party

# class PostForm(forms.Form):
  
#   my_field = forms.MultipleChoiceField(choices=Party.RULL_CHOICES, widget=forms.CheckboxSelectMultiple)

#   def choice_field(self):
#     if len(self.cleaned_data['my_field']) > 3:
#       raise forms.ValidationError('Select no more than 3.')
#     return self.cleaned_data['my_field']