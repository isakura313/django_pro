from django.shortcuts import render, redirect
from .models import TodoList, Category
def todo(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            # id_todo = request.POST["created"].strftime("%s")
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content,  due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo
            return redirect("/todo") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST.getlist('checkedbox') #checked todos to be deleted
            print(checkedlist)
            for i in range(len(checkedlist)):
                try:
                    print(int(checkedlist[i]))
                    todo = TodoList.objects.filter(id=int(checkedlist[i]))
                    todo.delete() #deleting todo
                except BaseException:
                    print("я не могу удалить")
                    # print(TodoList.objects.get(id=20))
    return render(request, "todo.html", {"todos": todos, "categories":categories})


def category(request):
    categories = Category.objects.all()  # getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            name = request.POST["name"] #имя нашей категории
            category = Category(name=name)
            category.save() #saving the todo
            return redirect("/category") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            cl = request.POST.getlist('check') #checked category to be deleted
            print(len(cl))
            for i in range(len(cl)):
                try:
                    print(int(cl[i]))
                    Categ = Category.objects.filter(id=int(cl[i]))
                    Categ.delete() #deleting todo
                except BaseException:
                    print("я не могу удалить")
                    # print(TodoList.objects.get(id=20))
    return render(request, "category.html", {"categories": categories})