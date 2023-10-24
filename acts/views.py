from django.shortcuts import render
from acts.models import Acts

# Create your views here.


def acts_index(request):
    acts = Acts.objects.all()
    context = {
        "acts": acts
    }
    return render(request, "acts/acts_index.html", context)


def acts_detail(request, pk):
    acts = Acts.objects.get(pk=pk)
    context = {
        "acts": acts
    }
    return render(request, "acts/acts_detail.html", context)
