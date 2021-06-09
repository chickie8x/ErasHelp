from django.shortcuts import render

# Create your views here.
from CreNumb.models import ToTrinh


def index(request):
    data = ToTrinh.objects.all()
    count = data.__len__()
    listObj =[]
    for d in data:
        obj = {}
        obj['id'] = d.id
        obj['identify']=str(d.id)+'/'+str(d.Created_on).split('-')[0]+'/'+str(d.RoomId)+'/'+str(d.TTId)
        obj['type']=d.TTId
        obj['department']=d.RoomId
        obj['user']=d.user
        obj['year']=str(d.Created_on).split('-')[0]
        obj['createdTime']=d.Created_on
        obj['title']=d.TTtitle
        listObj.append(obj)
    return render(request, 'CreNumb/index.html', context={'data':listObj, 'count':count})