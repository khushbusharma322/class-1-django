from django import forms
class userform (forms.Form):
    genchoice=(("male","Male"),("female","Female"))
    userid=forms.IntegerField(label="Id",label_suffix="",widget=forms.TextInput(attrs={'placeholder':'enter id', 'class':'idclass'}))
    username=forms.CharField(max_length=100,label="name",label_suffix="")
    userage=forms.IntegerField(label="age",label_suffix="")
    dob=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    #flieupload=forms.filefiels()
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=genchoice)
    courses=forms.CharField(choices=genchoice)
    password=forms.CharField(widget=forms.PasswordInput())


class Bookforms(forms.Form):
        catchoices=(("autobirography","autobirography"),("literature","literature"))
        bname=forms.CharField(max_length=20)
        bid=forms.IntegerField()
        authorname=forms.CharField(max_length=20)
        publishdate=forms.DateField(widget=forms.DateInput)
        price=forms.FloatField()
        

