from sqlite3 import Date

from django.shortcuts import render

# Create your views here.
from CreNumb.models import ToTrinh, Room


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
