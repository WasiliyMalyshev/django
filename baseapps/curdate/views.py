from django.shortcuts import render
import datetime

# Create your views here.

def curdate_index(request):


    context = {
        'datetime':datetime.datetime.now(),
        'tableum':[[i*j for j in range(1,10)] for i in range(1,10)],
        'programmer_day':datetime.datetime(datetime.datetime.now().year,1,1,0,0,0)+ datetime.timedelta(days=256),
    }
    return render(request, "curdate/index.html",context)