from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'heading' : 'Pelatihan'
    } 
    
    if request.method == 'POST':
        context['nama_model'] = request.POST['nama_model']
        context['num_epoch'] = request.POST['num_epoch']
    
    

    return render(request,'pelatihan.html', context)