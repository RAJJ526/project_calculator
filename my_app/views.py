from django.shortcuts import render
from django.views import View
# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')


class AboutView(View):
    def post(Self, request):
        if request.method=='POST':
            number_one=request.POST['number_one']
            number_two=request.POST['number_two']
            operation=request.POST['operation']
        if operation=='add':
            result=float(number_one)+float(number_two)
            context={'result':result}
            return render(request, 'index.html', context)
        
        elif operation=='subtract':
            result=float(number_one)-float(number_two)
            context={'result':result}
            return render(request, 'index.html', context)
        
        elif operation=='multiply':
            result=float(number_one)*float(number_two)
            context={'result':result}
            return render(request, 'index.html', context)
        
        elif operation=='divide':
            result=float(number_one)/float(number_two)
            context={'result':result}
            return render(request, 'index.html', context)
        
        else:
            return render(request, 'index.html')
