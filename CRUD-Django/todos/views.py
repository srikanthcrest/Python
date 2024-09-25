from django.shortcuts import render
from .models import ToDo
from .forms import ToDoForm
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView

# Create your views here.
 
def index(request):
    todoList = ToDo.objects.all().order_by('created_at')
    return render(request, 'todo/list.html', {'list': todoList})


def saveAction(request):
    if request.method == 'POST':
        # 
        # Manually extracting form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        
        # Basic validation checks
        if not title:
            return HttpResponse("Title is required", status=400)
        
        if not due_date:
            return HttpResponse("Due date is required", status=400)
        
        # Create and save the ToDo object
        todo = ToDo(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date,
            completed=False  # Default value
        )
        todo.save()

        return redirect('user_todos')
        # 
        form = request.POST
        print(form)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Associate the task with the logged-in user
            todo.save()
            return redirect('todo')
    else:
        form = ToDoForm()
    
    return render(request, 'todo/index.html', {'form': form})
    # todoform = TodoForm(request.POST or None)
    # if todoform.is_valid():
    #     todoform.save()

    #     return redirect('/')
    # return render(request, 'todo/index.html', {'form': todoform})


def editTodo(request, pk):

    pickTodo = ToDo.objects.get(pk=pk)

    editForm = TodoForm(request.POST or None, instance=pickTodo)
    if editForm.is_valid():
        editForm.save()
        return redirect('/')

    return render(request, 'todo/index.html', {'form': editForm})


def deleteAction(request, pk):

    pickTodo = ToDo.objects.get(pk=pk)
    pickTodo.delete()

    return redirect('/')


class TodoCreate(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # Handle the POST request
        print(request.data)  # Use request.data for DRF

        return HttpResponse("Your response1")