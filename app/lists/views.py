from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.forms import ItemForm
from lists.models import Item, List


def home_page(request):
    return render(request, 'lists/home.html', {'form': ItemForm()})


def view_list(request, list_id):
    itemlist = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=itemlist)
            return redirect(itemlist)
    return render(
        request,
        'lists/list.html',
        {'list': itemlist, 'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        itemlist = List.objects.create()
        form.save(for_list=itemlist)
        return redirect(itemlist)
    else:
        return render(request, 'lists/home.html', {"form": form})
