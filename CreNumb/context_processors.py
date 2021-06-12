from .models import Room, Year


def getBaseInfo(request):
    departments= Room.objects.all()
    years = Year.objects.all()
    context = {
        'departments': departments,
        'years': years
    }
    return context
