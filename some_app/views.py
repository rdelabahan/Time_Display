from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %I:%M %p", gmtime()),
        "timenow": datetime.now()
    }
    return render(request,'index.html', context)

# Create your views here.
