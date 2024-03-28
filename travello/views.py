from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

## static content
#     dest1 = Destination()
#     dest1.name = 'Mumbai'
#     dest1.desc = 'Good City'
#     dest1.price = 900
#     dest1.img = 'destination_1.jpg'
#     dest1.offer = False

#     dest2 = Destination()
#     dest2.name = 'Hydrabad'
#     dest2.desc = 'Biryani'
#     dest2.price = 800
#     dest2.img = 'destination_2.jpg'
#     dest2.offer = True

#     dest3 = Destination()
#     dest3.name = 'Banglore'
#     dest3.desc = 'IT City'
#     dest3.price = 850
#     dest3.img = 'destination_3.jpg'
#     dest3.offer = False

#     dests = [dest1, dest2,dest3]

#     return render(request, 'index.html',{'dests': dests})

    dests = Destination.objects.all()

    return render(request, 'index.html',{'dests': dests})