from django.shortcuts import render
import datetime

def template_view(request):
    dt = datetime.datetime.now()
    name='Khan'
    rollno=786
    marks=3000
    my_dict={'date':dt,'name':name,'rollno':rollno,'marks':marks}
    #my_dict = {'date':dt}
    #return render(request,'testapp/results.html',my_dict)
    #return render(request,'testapp/results.html',{'date':dt})
    return render(request, 'testapp/results.html', my_dict)





