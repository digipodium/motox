from django.shortcuts import render

# Create your views here.
def index_view(request):
    if request.method == 'POST':
        print("form submitted")
        form = request.POST
        print(form)
    return render(request, 'home/index.html',)