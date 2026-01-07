from django.shortcuts import render
from .models import Evento

# Create your views here.

def inicio_view(request):
    eventos = Evento.objects.order_by('fecha')
    return render(request, "inicio.html", {"eventos": eventos})

from django.shortcuts import get_object_or_404

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from .forms import PodcastForm, ReelForm


def evento_detalle(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    podcasts = evento.podcasts.all()
    reels = evento.reels.all()
    return render(request, "event_detail.html", {"evento": evento, "podcasts": podcasts, "reels": reels})


@staff_member_required
def upload_podcast(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            podcast = form.save(commit=False)
            podcast.evento = evento
            podcast.save()
            return redirect(reverse('evento_detalle', args=[evento.pk]))
    else:
        form = PodcastForm(initial={'evento': evento})
    return render(request, 'upload_podcast.html', {'form': form, 'evento': evento})


@staff_member_required
def upload_reel(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = ReelForm(request.POST, request.FILES)
        if form.is_valid():
            reel = form.save(commit=False)
            reel.evento = evento
            reel.save()
            return redirect(reverse('evento_detalle', args=[evento.pk]))
    else:
        form = ReelForm(initial={'evento': evento})
    return render(request, 'upload_reel.html', {'form': form, 'evento': evento})