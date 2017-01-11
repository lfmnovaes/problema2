from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Vuln

# ========== Forms =========

    # name = models.CharField(max_length=100)
    # desc = models.TextField()
    # afetado = models.CharField(max_length=50)
    # severidade = models.CharField(max_length=10)
    # status 


class VulnForm(ModelForm):
    class Meta:
        model = Vuln
        fields = ['name', 'desc', 'afetado', 'severidade', 'status']


# ========== Home =========

def home(request, template_name='vuln/home.html'):
    vulns = Vuln.objects.all()
    ctx = {}
    ctx['vulns'] = vulns
    return render(request, template_name, ctx)
    

# ========== vuln CRUD =========

def vuln_view(request, pk, template_name='vuln/vuln_view.html'):
    vuln = get_object_or_404(Vuln, pk=pk)
    ctx = {}
    ctx["vuln"] = vuln
    return render(request, template_name, ctx)

def vuln_create(request, template_name='vuln/vuln_form.html'):
    form = VulnForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vuln:home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def vuln_update(request, pk, template_name='vuln/vuln_form.html'):
    vuln = get_object_or_404(Vuln, pk=pk)
    form = VulnForm(request.POST or None, instance=vuln)
    if form.is_valid():
        form.save()
        return redirect('vuln:home')
    ctx = {}
    ctx["form"] = form
    ctx["vuln"] = vuln
    return render(request, template_name, ctx)

def vuln_delete(request, pk, template_name='vuln/vuln_confirm_delete.html'):
    vuln = get_object_or_404(Vuln, pk=pk)    
    if request.method=='POST':
        vuln.delete()
        return redirect('vuln:home')
    ctx = {}
    ctx["object"] = vuln
    ctx["vuln"] = vuln
    return render(request, template_name, ctx)