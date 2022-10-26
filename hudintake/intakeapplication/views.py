from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Monthly_Budget

def post_list(request):
    posts = Monthly_Budget.TotalExpense
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})

