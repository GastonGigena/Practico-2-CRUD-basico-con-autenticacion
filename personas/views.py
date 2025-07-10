from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Persona
from .forms import PersonaForm, CargaMasivaPersonaForm
from oficinas.models import Oficina
import csv
import io

class PersonaListView(ListView):
    model = Persona
    template_name = 'personas/lista.html'
    context_object_name = 'personas'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('q')
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) | 
                Q(apellido__icontains=busqueda)
            )
        return queryset

class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'personas/detalle.html'
    context_object_name = 'persona'

@login_required
def persona_crear(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona creada exitosamente')
            return redirect('personas:lista')
    else:
        form = PersonaForm()
    return render(request, 'personas/form.html', {'form': form, 'titulo': 'Crear Persona'})

@login_required
def persona_editar(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona actualizada exitosamente')
            return redirect('personas:detalle', pk=persona.pk)
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'personas/form.html', {'form': form, 'titulo': 'Editar Persona'})

@login_required
def persona_eliminar(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        persona.delete()
        messages.success(request, 'Persona eliminada exitosamente')
        return redirect('personas:lista')
    return render(request, 'personas/confirmar_eliminacion.html', {'persona': persona})

@login_required
def carga_masiva_personas(request):
    if request.method == 'POST':
        form = CargaMasivaPersonaForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            try:
                datos = archivo.read().decode('utf-8')
                reader = csv.reader(io.StringIO(datos))
                next(reader)  # Saltar header
                contador = 0
                for row in reader:
                    if len(row) >= 4:
                        try:
                            oficina = Oficina.objects.get(id=int(row[3]))
                            Persona.objects.create(
                                apellido=row[0].strip(),
                                nombre=row[1].strip(),
                                edad=int(row[2]),
                                oficina=oficina
                            )
                            contador += 1
                        except (Oficina.DoesNotExist, ValueError):
                            continue
                messages.success(request, f'Se cargaron {contador} personas exitosamente')
                return redirect('personas:lista')
            except Exception as e:
                messages.error(request, f'Error al procesar el archivo: {str(e)}')
    else:
        form = CargaMasivaPersonaForm()
    return render(request, 'personas/carga_masiva.html', {'form': form})