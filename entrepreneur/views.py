from django.shortcuts import render,redirect, get_object_or_404
from .models import Row, Cow, Duplicate_cow
from .forms import EntrepreneurForm, EntrepreneurEditForm,CowForm,CowEditForm,CowUpdateForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

# =--------------------ENTREPRENEUR---------------------------
def entrepreneur(request):
    context = {
        'rows':Row.objects.all()
    }
    return render(request,'entrepreneur/entrepreneur.html',context)


def add_entrepreneur(request):
    form = EntrepreneurForm()
    if request.method == 'POST':
        # pdict = request.POST.copy()
        form = EntrepreneurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form = EntrepreneurForm()
            return redirect('/entrepreneur')


    context = {
        'form' : form
    }
    return render(request,'entrepreneur/add_entrepreneur.html',context)


def view_entrepreneur(request,id):
    entrepreneur = get_object_or_404(Row, pk=id)
    own = entrepreneur.name_of_the_entrepreneur
    #print(own)
    context = {
        'row' : get_object_or_404(Row, pk=id),
        'cows': Cow.objects.filter(owner = own)
    }
    return render(request, 'entrepreneur/view_entrepreneur.html',context)


def edit_entrepreneur(request,id):
    row = get_object_or_404(Row,pk = id)
    
    if request.method == 'POST':
        edit_form = EntrepreneurEditForm(request.POST,request.FILES,instance= row)
    #     pdict = request.POST.copy()
    #     edit_form = EntrepreneurEditForm(pdict)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/entrepreneur')
        #edit_form = EntrepreneurEditForm()
    else:
        edit_form = EntrepreneurEditForm(instance= row)


    context = {
        'edit_form' : edit_form
    }
    return render(request, 'entrepreneur/edit_entrepreneur.html',context)

def search(request):
    query = request.POST.get('search','')
    if query:
        queryset = (Q(name_of_the_entrepreneur__icontains = query)) | (Q(district__icontains = query)) | (Q(village__icontains = query)) | (Q(upazilla__icontains = query)) | (Q(mobile__icontains = query))
        results = Row.objects.filter(queryset).distinct()
    else:
        results = []
    context = {
        'results' : results
    }
    return render(request,'entrepreneur/search.html',context)

def search_entrepreneur_cow(request,id):
    query = request.POST.get('search_entrepreneur_cow','')
    row = get_object_or_404(Row,pk = id)
    
    if query:
        queryset =  (Q(name_of_cow__icontains = query)) | (Q(breed__icontains = query)) | (Q(color__icontains = query)) | (Q(weight__icontains = query)) | (Q(purchase_date__icontains = query)) | (Q(date_of_birth__icontains=query))
        results = Cow.objects.filter(queryset).distinct()
    else:
        results = []
    
    context = {
        'results': results,
        'row': row
    }
    return render(request,'entrepreneur/search_entrepreneur_cow.html',context)

# ===============================COW==========================
def add_cow(request,id):
    entrepreneur = get_object_or_404(Row,pk=id)
    name = entrepreneur.name_of_the_entrepreneur
    cow_form = CowForm(initial={'owner': entrepreneur.name_of_the_entrepreneur})
    
    if request.method == 'POST':
        # pdict = request.POST.copy()
        cow_form = CowForm(request.POST,request.FILES,initial={'owner': entrepreneur.name_of_the_entrepreneur})
        print(cow_form)
        if cow_form.is_valid():
            cow_form.save()
            cow_form = CowForm(initial={'owner': entrepreneur.name_of_the_entrepreneur})
            element = Row.objects.get(name_of_the_entrepreneur = name)
            #print(element)
            return redirect(reverse('view_entrepreneur', args = [element.id]))


    context = {
        'cow_form' : cow_form,
        'row' : entrepreneur,
        'name' : name
    }
    return render(request,'entrepreneur/add_cow.html',context)



def cow(request):
    context = {
        'cows':Cow.objects.all()
    }
    return render(request,'entrepreneur/cow.html',context)

def edit_cow(request,id):
    cow = get_object_or_404(Cow,pk=id)
    if request.method == 'POST':
        edit_cow_form = CowEditForm(request.POST,request.FILES,instance= cow)
    #     pdict = request.POST.copy()
    #     edit_form = EntrepreneurEditForm(pdict)
        if edit_cow_form.is_valid():
            edit_cow_form.save()
            own = cow.owner
            element = Row.objects.get(name_of_the_entrepreneur = own)
            #print(element)
            return redirect(reverse('view_entrepreneur', args = [element.id]))
        #edit_form = EntrepreneurEditForm()
    else:
        edit_cow_form = CowEditForm(instance= cow)


    context = {
        'edit_cow_form' : edit_cow_form
    }
    return render(request, 'entrepreneur/edit_cow.html',context)




def view_cow(request,id):
    cow = get_object_or_404(Cow, pk = id)
    print(cow.name_of_cow)
    name = cow.name_of_cow
    context = {
        'cow': cow,
        'duplicate_cows':Duplicate_cow.objects.all()
    }
    print(context['duplicate_cows'][0].updated_image)
    return render(request,'entrepreneur/view_cow.html',context)
def search_cow(request):
    query = request.POST.get('search_cow','')
    if query:
        queryset = (Q(name_of_cow__icontains = query)) | (Q(breed__icontains = query)) | (Q(color__icontains = query)) | (Q(weight__icontains = query)) | (Q(purchase_date__icontains = query)) | (Q(date_of_birth__icontains=query))
        results = Cow.objects.filter(queryset).distinct()
    else:
        results = []
    context = {
        'results': results
    }
    return render(request,'entrepreneur/search_cow.html',context)

def update_cow(request,id):
    cows = get_object_or_404(Cow,pk = id)
    #print(cow.name_of_cow)
    cow_update_form = CowUpdateForm(initial={'cow_name':cows.name_of_cow})
    if request.method == 'POST':
        
        cow_update_form = CowUpdateForm(request.POST, request.FILES)
        if cow_update_form.is_valid():
            cow_update_form.save()
            cow_update_form = CowUpdateForm(initial={'cow_name':cows.name_of_cow})
            own = cows.owner
            element = Row.objects.get(name_of_the_entrepreneur = own)
            #print(element)
            return redirect(reverse('view_entrepreneur', args = [element.id]))
    


    context = {
        'cow_update_form' : cow_update_form,
        'cows' : cows
    }
    return render(request,'entrepreneur/update_cow.html',context)