from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import todo_model
from .forms import TodoModelForm

# Create your views here.
def todo_list(request):
    all_tasks=todo_model.objects.all()   
    if request.method=='POST':
        form=TodoModelForm(request.POST) 

        if form.is_valid():
            form.save()     
    
    else:                   
        form=TodoModelForm()
    return render(request,"todo_app/todo_list_temp.html",{
        "form":form, 
        "all_tasks":all_tasks
        })



def delete_task(request,id):
    task_to_delete=todo_model.objects.get(id=id)#Fetching the data which we want to delete in object.
    task_to_delete.delete()#Deleting the particular object
    return HttpResponseRedirect("/")#Redirecting to list of task

def edit_task(request,id):
    edit_task=todo_model.objects.get(id=id)#Getting the task which we want to edit and update
    form=TodoModelForm(request.POST or None,instance=edit_task)#Making the object of model form, collecting data in the form,setting the fetch value in the form
    if form.is_valid():#cheking if new submitted data is valid
        form.save() #if data is valid save
        return HttpResponseRedirect("/") # and redirect to all task
    return render(request,"todo_app/todo_list_edit.html",{
         "form":form,
         })#if data is not valid rendering the same form with enterd data


  


       