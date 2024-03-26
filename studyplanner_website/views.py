from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,"index.html",{})

def todo_list(request):
    return render(request,"todo_list.html",{"days":["why","do","I need","to","transpose"],"tasklen":"why is this a string"})
