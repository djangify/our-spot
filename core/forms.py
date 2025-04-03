from django import forms

class ReportForm(forms.Form):
    REPORT_CONTENT_TYPES = [
        ('photo', 'A photo'),
        ('profile', 'A member profile'),
        ('comment', 'A comment'),
    ]
    
    REPORT_TYPES = [
        ('location', 'Location/Photo'),
        ('profile', 'Profile'),
        ('comment', 'Comment'),
    ]
    
    REASON_CHOICES = [
        ('', 'Please select a reason'),
        ('inappropriate', 'Inappropriate Content'),
        ('spam', 'Spam Content'),
        ('offensive', 'Offensive Language'),
        ('harassment', 'Harassment'),
        ('copyright', 'Copyright Violation'),
        ('other', 'Other'),
    ]
    
    report_content_type = forms.ChoiceField(choices=REPORT_CONTENT_TYPES)
    report_type = forms.ChoiceField(choices=REPORT_TYPES)
    reason = forms.ChoiceField(choices=REASON_CHOICES)
    details = forms.CharField(widget=forms.Textarea)