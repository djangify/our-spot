from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason', 'details']
        widgets = {
            'reason': forms.Select(choices=[
                ('inappropriate', 'Inappropriate Content'),
                ('spam', 'Spam'),
                ('offensive', 'Offensive Language'),
                ('harassment', 'Harassment'),
                ('copyright', 'Copyright Violation'),
                ('other', 'Other')
            ]),
            'details': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Please provide additional details about your report...'})
        }
