from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')