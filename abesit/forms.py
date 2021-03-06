from django import forms




QUIZ_CHOICES =[
    ('C/C++','C/C++'),
    ('JAVA','JAVA'),
    ('python','PYTHON'),
    ('dbms/os','DBMS/OS'),
    ('None','NONE')
]
YEAR_CHOICES = [
('1','1'),
('2','2'),
('3','3'),
('4','4'),

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
    Roll_No = forms.CharField(max_length=12)
    Contact_No = forms.CharField(max_length=11)
    CSI = forms.CharField(required=False,max_length=10)
    College_Code = forms.CharField(max_length=3)
    Year = forms.ChoiceField(choices = YEAR_CHOICES,widget = forms.RadioSelect())
    Quiz = forms.ChoiceField(choices=QUIZ_CHOICES,widget=forms.RadioSelect())
    Gaming = forms.ChoiceField(choices=GAMING_CHOICES,widget=forms.RadioSelect())
    Coding = forms.ChoiceField(choices=CODING_CHOICES,widget=forms.RadioSelect())
    Webdesigning = forms.ChoiceField(choices=DESIGN_CHOICES,widget=forms.RadioSelect())
    Androiddevelopment = forms.ChoiceField(choices=ANDROID_CHOICES,widget=forms.RadioSelect())
    Groupdiscussion = forms.ChoiceField(choices=DISCUSSION_CHOICES,widget=forms.RadioSelect())
