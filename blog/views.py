from django.shortcuts import render
from django.utils import timezone
from .models import Implementodep
from django.shortcuts import render, get_object_or_404
from .forms import RegistrationForm
from .forms import ImplementodepForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def Index(request):
    Implementodeps = Implementodep.objects.all().order_by('pk')
    return render(request,'blog/index.html', {'Implementodeps': Implementodeps})
def Registro(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            Implementodep = form.save(commit=False)
            Implementodep.save()
            return redirect('Galeria')
    else:
        form = RegistrationForm()
    return render(request, 'blog/Registro.html', {'form': form})
def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('Registro')
    else:
        form = AuthenticationForm()
    return render(request,'blog/Login.html',{'form':form})
#def Implementodep_detail(request, pk):
#    Implementodeps = get_object_or_404(Implementodep, pk=pk)
#    return render(request, 'blog/Implementodep_detail.html', {'Implementodeps': Implementodeps})
#def Implementodep_edit(request, pk):
#    Implementodeps = get_object_or_404(Implementodep, pk=pk)
#    if request.method == "POST":
#        form = ImplementodepForm(request.POST, instance=Implementodeps)
#        if form.is_valid():
#            Implementodeps = form.save(commit=False)
#            Implementodeps.estado = 'ARRENDADO'
#            Implementodeps.save()
#            return redirect('Index')
#    else:
#        form = ImplementodepForm(instance=Implementodeps)
#    return render(request, 'blog/Implementodep_edit.html', {'form': form})
#def Factura_edit(request, pk):
#    Facturas = get_object_or_404(Factura, pk=pk)
#    if request.method == "POST":
#        form = FacturaForm(request.POST, instance=Facturas)
#        if form.is_valid():
#            Facturas = form.save(commit=False)
#            Facturas.estado = 'ARRENDADO'
#            Facturas.save()
#            return redirect('Index')
#    else:
#        form = FacturaForm(instance=Facturas)
#    return render(request, 'blog/Factura_edit.html', {'form': form})