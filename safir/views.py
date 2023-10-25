from django.shortcuts import render
import pytz
from .models import *
from django.shortcuts import redirect
from datetime import datetime

# Create your views here.
def update_link(request):
    vedio = Add_video.objects.get(id=1)
    
    tz = pytz.timezone('Asia/Damascus')
    a=[Linke.objects.values_list('count_of_clients','pk','now','expiration_date')]
    now = datetime.now(tz)
    for i in a:
        i=min(i)
        
        if   now  < i[3]:

            i=i[1]
            count_of_client,created = Linke.objects.get_or_create(pk=i,defaults={'count_of_clients':0})
        
            if  request.method == 'POST':
                count_of_client.count_of_clients += 1
                count_of_client.save()
                return redirect(count_of_client.link)
        else:
            
            
            i=i[1]
            count_of_client,created = Linke.objects.get_or_create(pk=i,defaults={'likes':0})
            count_of_client.delete()
            
          
          
    return render (request,'index.html',context={'vedio':vedio,'count_of_client':count_of_client,'crated':created})
           

