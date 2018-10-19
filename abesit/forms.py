from django import forms




QUIZ_CHOICES =[
    ('C/C++/Java','C/C++/Java'),
    ('python','PYTHON'),
    ('dbms/os','DBMS/OS'),
    ('None','NONE')
]
GAMING_CHOICES = [
    ('NFS','NFS'),
('Counterstrike','COUNTERSTRIKE'),
('Pubg','PUBG'),
    ('None','NONE'),
]
CODING_CHOICES = [
('C','C'),
('c++','C++'),
('java','JAVA'),
('None','NONE'),
 ]
DESIGN_CHOICES =[
('Participate','PARTICIPATE'),
('No','NO'),
 ]
ANDROID_CHOICES =[
('Participate','PARTICIPATE'),
('No','NO'),
 ]
DISCUSSION_CHOICES = [
('Participate','PARTICIPATE'),
('No','NO'),
 ]


class RegisterForm(forms.Form):
    Name = forms.CharField(max_length=20)
    Email= forms.EmailField(max_length=70)
    Contact_No = forms.CharField(max_length=10)
    CSI = forms.CharField(required=False,max_length=8)
    College_Code = forms.CharField(max_length=3)
    Quiz = forms.ChoiceField(required=False,choices=QUIZ_CHOICES,widget=forms.RadioSelect())
    Gaming = forms.ChoiceField(required=False,choices=GAMING_CHOICES,widget=forms.RadioSelect())
    Coding = forms.ChoiceField(required=False,choices=CODING_CHOICES,widget=forms.RadioSelect())
    Webdesigning = forms.ChoiceField(required=False,choices=DESIGN_CHOICES,widget=forms.RadioSelect())
    Androiddevelopment = forms.ChoiceField(required=False,choices=ANDROID_CHOICES,widget=forms.RadioSelect())
    Groupdiscussion = forms.ChoiceField(required=False,choices=DISCUSSION_CHOICES,widget=forms.RadioSelect())
