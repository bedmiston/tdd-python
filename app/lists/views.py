from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request, list_id):
    itemlist = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list': itemlist})


def new_list(request):
    itemlist = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=itemlist)
    return redirect('/lists/%d/' % (itemlist.id,))


def add_item(request, list_id):
    itemlist = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=itemlist)
    return redirect('/lists/%d/' % (itemlist.id,))
