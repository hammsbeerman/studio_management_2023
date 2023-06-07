from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import KruegerJobDetailForm
from .models import KruegerJobDetail

# Create your views here.

def newjob(request):
    form = KruegerJobDetailForm(request.POST or None)
    total_invoices = KruegerJobDetail.objects.count()
    queryset = KruegerJobDetail.objects.filter(company='LK').order_by('-dateentered')[:6]
    if form.is_valid():
        #print (form)
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/quotes/kruegerprint')
    context = {
        "form": form,
        "title": "New Job",
        "total_invoices": total_invoices,
		"queryset": queryset,
    }
    return render(request, "quotes/kruegerprint.html", context)
