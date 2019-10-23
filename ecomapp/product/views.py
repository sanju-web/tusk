from django.shortcuts import get_object_or_404,render
# Create your views here.
from .models import Product


def dummy_product():
    return Product(id=0,name='',price=0.0,qty=0,category='',remarks='',brand='',vendor='')

def welcome_product_page(req):
    return render (req,'product.html',{'prod':dummy_product(),"products":Product.objects.all()})

def save_or_update_product(req):
    if int(req.POST['pid'])==0:
        prod=Product(name=req.POST['pnm'],
                     price=req.POST['ppr'],
                     qty=req.POST['pqt'],
                     category=req.POST['pcat'],
                     remarks=req.POST['pre'],
                     brand=req.POST['pbr'],
                     vendor=req.POST['pve'])
        amsg="Product <{}> record save successfully...."
    else:
        prod = Product(id=req.POST['pid'],
                       name=req.POST['pnm'],
                       price=req.POST['ppr'],
                       qty=req.POST['pqt'],
                       category=req.POST['pcat'],
                       remarks=req.POST['pre'],
                       brand=req.POST['pbr'],
                       vendor=req.POST['pve'])
        amsg="Product <{}> record updated successfuly"
    prod.save()
    return render (req,'product.html',{'prod':dummy_product(),
                                       "products":Product.objects.all(),
                                       "msg":amsg.format(prod.id)})

def fetct_product_for_edit(req,pid):
    return render (req,'product.html',{'prod':dummy_product(),
                                       "products":Product.objects.get(pid),})

def remove_product_record(req,pid):
    Product.objects.get(id=pid).delete()
    return render (req,'product.html',{'prod':dummy_product(),
                                       "products":Product.objects.all(),
                                       "msg":"Product <{}> record remove from database".format(pid)})
