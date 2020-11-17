from django.shortcuts import render
from .models import Destination
from .models import Subscribe
from .models import Contact

# from . models import Destination
# from . models import Subscribe
# from . models import Contact

# Create your views here.
# Data comming Dynamically from database
def index(request): 
      dests = Destination.objects.all() # Assinging all objects of the 'Destination' to 'dests' variabel because
                                        # Because we want to use each object in html page dynamically 
                                        # Example: {dests.name}, {dests.price} .....so on
                                    

      return render(request,'index.html',{'dests':dests})


def esubscribe(request):
      subs = Subscribe.objects.all()
      
      return render(request,'subscribe.html', {'subs':subs})

def contact(request):
      # cont = Contact.objects.all()
      if request.method== "POST":
            name = request.POST['name']
            mobile = request.POST['mobile']
            email = request.POST['email']
            # textarea = request.POST['textarea']
            ins = Contact(name=name, mobile=mobile, email=email )
            ins.save()
            print('my data is written and saved to db')
            

      
      return render(request, 'contacts.html')




# Data comming from code statically:  

# def index(request):     
#       dest1 = Destination()
#       dest1.name="America"
#       dest1.desc = "A brand city"
#       dest1.price = 8000
#       dest1.img = 'destination_1.jpg'
#       dest1.offer = True

#       dest2 = Destination()
#       dest2.name = "Goa"
#       dest2.desc = "A city never sleep"
#       dest2.price = 6000
#       dest2.img = 'destination_3.jpg'
#       dest2.offer = False

#       dest3 = Destination()
#       dest3.name="Goa"
#       dest3.desc = "A city never sleep"
#       dest3.price = 6000
#       dest3.img = 'destination_3.jpg'
#       dest3.offer = False

#       dest4 = Destination()
#       dest4.name = "Delhi"
#       dest4.desc = "India gate is the great place to visit in india "
#       dest4.price = 6000
#       dest4.img = 'destination_4.jpg'
#       dest4.offer = False

#       dests = [dest1, dest2, dest3, dest4]



#       return render(request,'index.html',{'dests':dests})
