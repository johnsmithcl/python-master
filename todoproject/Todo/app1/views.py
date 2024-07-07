from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Todo
from .forms import Todoform



class Listview(ListView):
    model=Todo
    template_name='home.html'
    context_object_name = 'show'

class Detailview(DetailView):
    model=Todo
    template_name='detail.html'
    context_object_name = 'i'

class Updateview(UpdateView):
    model=Todo
    template_name='edit.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('Detailview',kwargs={'pk':self.object.id})



# Create your views here.

def home(request):
    if request.method=='POST':
        name= request.POST.get('n1')
        priority= request.POST.get('n2')
        date = request.POST.get('n3')
        task=Todo(name=name,priority=priority,date=date)
        task.save()
    show=Todo.objects.all()
    return render(request,'home.html',{'show':show})

def delete(request,id):
    if request.method == 'POST':
        task=Todo.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task = Todo.objects.get(id=id)
    f=Todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':f})
