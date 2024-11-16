from django import forms
from django.forms import ModelForm, widgets
from .models import Row, Cow, Duplicate_cow
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class DateInput(forms.DateInput):
    input_type = 'date'

class EntrepreneurForm(ModelForm):
    class Meta:
        model = Row
        fields = "__all__"
        widgets = {
            'name_of_the_entrepreneur' : forms.TextInput(attrs = {'placeholder':'Name of the Entrepreneur','class' : 'form_box_inputs'}),
            'district' : forms.TextInput(attrs = {'placeholder':'District','class' : 'form_box_inputs'}),
            'upazilla' : forms.TextInput(attrs = {'placeholder':'Upazilla','class' : 'form_box_inputs'}),
            'village' : forms.TextInput(attrs = {'placeholder':'Village','class' : 'form_box_inputs'}),
            'mobile' : forms.NumberInput(attrs = {'placeholder':'Mobile','class' : 'form_box_inputs'}),
            'image': forms.FileInput(attrs={'placeholder':'Image','class':'form_box_inputs'})
           
        }
        labels = {
            'name_of_the_entrepreneur' : 'Name',
        }

class EntrepreneurEditForm(ModelForm):
    class Meta:
        model = Row
        fields = "__all__"
        widgets = {
            'name_of_the_entrepreneur' : forms.TextInput(attrs = {'placeholder':'Name of the Entrepreneur','class' : 'form_box_inputs'}),
            'district' : forms.TextInput(attrs = {'placeholder':'District','class' : 'form_box_inputs'}),
            'upazilla' : forms.TextInput(attrs = {'placeholder':'Upazilla','class' : 'form_box_inputs'}),
            'village' : forms.TextInput(attrs = {'placeholder':'Village','class' : 'form_box_inputs'}),
            'mobile' : forms.NumberInput(attrs = {'placeholder':'Mobile','class' : 'form_box_inputs'}),
            'image': forms.FileInput(attrs={'placeholder':'Image','class':'form_box_inputs'})
           
        }
        labels = {
            'name_of_the_entrepreneur' : 'Name',
        }
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class CowForm(ModelForm):
 
    class Meta:
        model = Cow
        fields = ['name_of_cow','purchase_date','breed','color','weight','date_of_birth','image','owner']
        widgets = {
            'name_of_cow':forms.TextInput(attrs={'placeholder':'Name of The Cow',"class":'form_box_inputs'}),
            'owner':forms.TextInput(attrs={"class":'form_box_inputs'}),
            'purchase_date':DateInput(attrs={'placeholder':'Date of Purchase',"class":'form_box_inputs'}),
            'breed':forms.TextInput(attrs={'placeholder':'Breed of the Cow',"class":'form_box_inputs'}),
            'color':forms.TextInput(attrs={'placeholder':'Color of the Cow',"class":'form_box_inputs'}),
            'weight':forms.NumberInput(attrs={'placeholder':'Weight of the Cow',"class":'form_box_inputs'}),
            'date_of_birth':DateInput(attrs={"class":'form_box_inputs'}),
            'image': forms.FileInput(attrs={'placeholder':'Image','class':'form_box_inputs'})


        }
        labels = {
            'name_of_cow' : 'Name',
            'owner': 'owner'
        }
class CowEditForm(ModelForm):
    class Meta:
        model = Cow
        fields=['name_of_cow','purchase_date','breed','color','weight','date_of_birth','image']
        widgets={
            'name_of_cow':forms.TextInput(attrs={'placeholder':'Name of The Cow',"class":'form_box_inputs'}),
            'purchase_date':DateInput(attrs={'placeholder':'Date of Purchase',"class":'form_box_inputs'}),
            'breed':forms.TextInput(attrs={'placeholder':'Breed of the Cow',"class":'form_box_inputs'}),
            'color':forms.TextInput(attrs={'placeholder':'Color of the Cow',"class":'form_box_inputs'}),
            'weight':forms.NumberInput(attrs={'placeholder':'Weight of the Cow',"class":'form_box_inputs'}),
            'date_of_birth':DateInput(attrs={'placeholder':'Date of Birth',"class":'form_box_inputs'}),
            'image': forms.FileInput(attrs={'placeholder':'Image','class':'form_box_inputs'})
        }
        labels = {
            'name_of_cow' : 'Name'
        }

class CowUpdateForm(ModelForm):
    class Meta:
        model = Duplicate_cow
        fields = ['cow_name','month','year','dewarming_date','torka','torka_date','kurha','kurha_date','badla','badla_date','name_of_the_disease',
                  'details_on_the_disease','medications','monthly_food_expenditure','food_consumed','percentage_grass','percentage_solid','current_weight','updated_image']
        widgets = {
            'cow_name':forms.TextInput(attrs={"class":'form_box_inputs'}),
            'month':forms.TextInput(attrs={'placeholder':'Month',"class":'form_box_inputs'}),
            'year':forms.TextInput(attrs={'placeholder':'Year',"class":'form_box_inputs'}),
            'dewarming_date':DateInput(attrs={'placeholder':'Dewarming Date',"class":'form_box_inputs'}),
            'torka':forms.TextInput(attrs={'placeholder':'Torka',"class":'form_box_inputs'}),
            'torka_date':DateInput(attrs={'placeholder':'Torka Date',"class":'form_box_inputs'}),
            'kurha':forms.TextInput(attrs={'placeholder':'Kurha',"class":'form_box_inputs'}),
            'kurha_date':DateInput(attrs={'placeholder':'Kurha Date',"class":'form_box_inputs'}),
            'badla':forms.TextInput(attrs={'placeholder':'Badla',"class":'form_box_inputs'}),
            'badla_date':DateInput(attrs={'placeholder':'Badla Date',"class":'form_box_inputs'}),
            'name_of_the_disease':forms.TextInput(attrs={'placeholder':'Name of The Disease',"class":'form_box_inputs'}),
            'details_on_the_disease':forms.TextInput(attrs={'placeholder':'Details on The Disease',"class":'form_box_inputs'}),
            'medications':forms.TextInput(attrs={'placeholder':'Medications',"class":'form_box_inputs'}),
            'monthly_food_expenditure':forms.TextInput(attrs={'placeholder':'Monthly Food Expenditure(Taka)',"class":'form_box_inputs'}),
            'food_consumed':forms.TextInput(attrs={'placeholder':'Monthly Food Consumed','class':'form_box_inputs'}),
            'percentage_grass':forms.NumberInput(attrs={'placeholder':'Percentage of Grass(in %)','class':'form_box_inputs'}),
            'percentage_solid':forms.NumberInput(attrs={'placeholder':'Percentage of Solid Food(in %)','class':'form_box_inputs'}),
            'current_weight':forms.NumberInput(attrs={'placeholder':'Current Weight(in Kg)',"class":'form_box_inputs'}),
            'updated_image':forms.FileInput(attrs={'placeholder':'Upload Image',"class":'form_box_inputs'}),

        }
        labels = {
            'cow_name' : 'cow_name',
            'month':'Month',
            'year':'Year',
            'dewarming_date':'Dewarming Date',
            'torka':'Torka',
            'torka_date':'Date',
            'kurha':'Kurha',
            'kurha_date':'Date',
            'badla':'Badla',
            'badla_date':'Date',
            'name_of_the_disease':'Disease',
            'details_on_the_disease':'Details',
            'medications':'Medications',
            'monthly_food_expenditure':'Monthly Food Expenditure',
            'food_consumed': 'Monthly Food Consumed',
            'percentage_grass':'Percentage of Grass',
            'percentage_solid':'Percentage of Solid',
            'current_weight':'Current Weight',
            'updated_image':'Upload Image',
        }