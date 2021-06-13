from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate,user_logged_out
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your views here.
from CreNumb.models import ToTrinh, Room


@login_required
def index(request):
    data = ToTrinh.objects.all()
    rooms = Room.objects.all()
    room_dict = {}
    for room in rooms:
        room_dict[room.RoomID] = room.quantity
    count = data.__len__()
    listObj = []
    for d in data:
        obj = {}
        room = str(d.RoomId)
        room_quantity = room_dict[room]
        obj['identify'] = str(d.idByYear) + '/' + str(d.Created_on).split('-')[0] + '/' + str(d.RoomId) + '/' + str(
            d.TTId) + '/' + str(room_quantity)
        obj['type'] = d.TTId
        obj['department'] = d.RoomId
        obj['user'] = d.user
        obj['year'] = str(d.Created_on).split('-')[0]
        obj['createdTime'] = str(d.Created_on)
        obj['title'] = d.TTtitle
        listObj.append(obj)
    return render(request, 'CreNumb/index.html', context={'data': listObj, 'count': count})


@login_required(login_url='/login/')
def filterByYear(request, year):
    beginDate = year + '-01-01'
    endDate = year + '-12-31'
    filterData = ToTrinh.objects.filter(Created_on__range=(beginDate, endDate))
    rooms = Room.objects.all()
    room_dict = {}
    for room in rooms:
        room_dict[room.RoomID] = room.quantity
    listObj = []
    for d in filterData:
        obj = {}
        room = str(d.RoomId)
        room_quantity = room_dict[room]
        obj['identify'] = str(d.idByYear) + '/' + str(d.Created_on).split('-')[0] + '/' + str(d.RoomId) + '/' + str(
            d.TTId) + '/' + str(room_quantity)
        obj['type'] = d.TTId
        obj['department'] = d.RoomId
        obj['user'] = d.user
        obj['year'] = str(d.Created_on).split('-')[0]
        obj['createdTime'] = str(d.Created_on)
        obj['title'] = d.TTtitle
        listObj.append(obj)
    return render(request, 'CreNumb/filterByYear.html', context={'filter': listObj, 'year': year})

@login_required(login_url='/login/')
def filterByDepartment(request, department):
    filterData = ToTrinh.objects.filter(RoomId__RoomID=department)
    rooms = Room.objects.all()
    room_dict = {}
    for room in rooms:
        room_dict[room.RoomID] = room.quantity
    listObj = []
    for d in filterData:
        obj = {}
        room = str(d.RoomId)
        room_quantity = room_dict[room]
        obj['identify'] = str(d.idByYear) + '/' + str(d.Created_on).split('-')[0] + '/' + str(d.RoomId) + '/' + str(
            d.TTId) + '/' + str(room_quantity)
        obj['type'] = d.TTId
        obj['department'] = d.RoomId
        obj['user'] = d.user
        obj['year'] = str(d.Created_on).split('-')[0]
        obj['createdTime'] = str(d.Created_on)
        obj['title'] = d.TTtitle
        listObj.append(obj)
    return render(request, 'CreNumb/filterByDepartment.html', context={'filter': listObj, 'department': department})

def loginView(request):
    if request.method =='POST':
        username=request.POST['username']
        password = request.POST['password']
        nexturl = request.POST['next']
        user = authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            messages.success(request,'Logged in as '+str(request.user))
            if 'next' in request.GET:
                return HttpResponseRedirect(nexturl)
            else:
                return HttpResponseRedirect('/')
        else:
            messages.warning(request,'Login failed , check again username and password')
            return HttpResponseRedirect('/login/')

    else:
        return render(request,'CreNumb/login.html',{})


def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

@receiver(user_logged_out)
def on_user_logged_out(sender, request, user, **kwargs):
    if not user:
        mes = ''
    else:
        mes = 'You have been logged out'
    messages.add_message(request, messages.WARNING, mes)


def registerView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if username and password and email:
            user,created = User.objects.get_or_create(username=username,email=email,password=password)
            if created:
                user.set_password(password)
                user.save()
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                HttpResponseRedirect('/')
        else:
            print('incorrect input information')
            return HttpResponseRedirect('/login/')
    else:
        return render(request,'CreNumb/register.html',{})