from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Oficina
from .forms import OficinaForm, CargaMasivaOficinaForm
import csv
import io

class OficinaListView(ListView):
    model = Oficina
    template_name = 'oficinas/lista.html'
    context_object_name = 'oficinas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('q')
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) | 
                Q(nombre_corto__icontains=busqueda)
            )
        return queryset

class OficinaDetailView(DetailView):
    model = Oficina
    template_name = 'oficinas/detalle.html'
    context_object_name = 'oficina'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personas'] = self.object.personas.all()
        return context

@login_required
def oficina_crear(request):
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oficina creada exitosamente')
            return redirect('oficinas:lista')
    else:
        form = OficinaForm()
    return render(request, 'oficinas/forms.html', {'form': form, 'titulo': 'Crear Oficina'})

@login_required
def oficina_editar(request, pk):
    oficina = get_object_or_404(Oficina, pk=pk)
    if request.method == 'POST':
        form = OficinaForm(request.POST, instance=oficina)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oficina actualizada exitosamente')
            return redirect('oficinas:detalle', pk=oficina.pk)
    else:
        form = OficinaForm(instance=oficina)
    return render(request, 'oficinas/form.html', {'form': form, 'titulo': 'Editar Oficina'})

@login_required
def oficina_eliminar(request, pk):
    oficina = get_object_or_404(Oficina, pk=pk)
    if request.method == 'POST':
        oficina.delete()
        messages.success(request, 'Oficina eliminada exitosamente')
        return redirect('oficinas:lista')
    return render(request, 'oficinas/confirmar_eliminacion.html', {'oficina': oficina})

@login_required
def carga_masiva_oficinas(request):
    if request.method == 'POST':
        form = CargaMasivaOficinaForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            try:
                datos = archivo.read().decode('utf-8')
                reader = csv.DictReader(io.StringIO(datos))
                contador = 0
                for row in reader:
                    if 'nombre' in row and 'nombre_corto' in row:
                        Oficina.objects.create(
                            nombre=row['nombre'].strip(),
                            nombre_corto=row['nombre_corto'].strip()
                        )
                        contador += 1
                messages.success(request, f'Se cargaron {contador} oficinas exitosamente')
                return redirect('oficinas:lista')
            except Exception as e:
                messages.error(request, f'Error al procesar el archivo: {str(e)}')
    else:
        form = CargaMasivaOficinaForm()
    return render(request, 'oficinas/carga_masiva.html', {'form': form})
