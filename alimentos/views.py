from django.shortcuts import render, redirect, get_object_or_404
from .models import Alimento
from .forms import AlimentoForm

def alimento_list(request):
	alimentos = Alimento.objects.all()
	return render(request, 'alimentos/alimento_list.html', {'alimentos': alimentos})

def alimento_create(request):
	if request.method == 'POST':
		form = AlimentoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('alimento_list')
	else:
		form = AlimentoForm()
	return render(request, 'alimentos/alimento_form.html', {'form': form})

def alimento_update(request, pk):
	alimento = get_object_or_404(Alimento, pk=pk)
	if request.method == 'POST':
		form = AlimentoForm(request.POST, instance=alimento)
		if form.is_valid():
			form.save()
			return redirect('alimento_list')
	else:
		form = AlimentoForm(instance=alimento)
	return render(request, 'alimentos/alimento_form.html', {'form': form})

def alimento_delete(request, pk):
	alimento = get_object_or_404(Alimento, pk=pk)
	if request.method == 'POST':
		alimento.delete()
		return redirect('alimento_list')
	return render(request, 'alimentos/alimento_confirm_delete.html', {'alimento': alimento})
