from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Travel
from .forms import TravelForm



# Create your views here.
class TravelDetailView(DetailView):
    model = Travel
    template_name = "travelapp/detail.html"  
    context_object_name = 'travel'

class TravelListView(ListView):
    model = Travel
    template_name = "travelapp/list.html"  
    context_object_name = 'travels'


    def get_queryset(self):
        return  Travel.objects.filter(Person__gt =4) 
 
    
def home(request):
        return render(request, 'travelapp/home.html')
    
def travels_list(request):
        travels = Travel.object.all()
        return render(request, 'travelapp/travels_list.html', {'travels': travels})
    
def travel_create(request):
        if request.method == 'POST':
            form = TravelForm(request.POST)   
            if form.is_valid():
                form.save()
                return redirect('travels_list')
        else:
            form = TravelForm()
            return render(request, 'travelapp/travel_create.html', {'form': form})