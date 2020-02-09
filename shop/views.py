from django.shortcuts import render , get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

def search(request):
    try:
        q=request.GET.get('q')
    except:
        q=None
    if q:
        products = Product.objects.filter(name__icontains=q)
        context = {'query':q,'products':products}
        template = 'shop/products/results.html'
    else:
        template='shop/products/list.html'
        context = {}
    return render(request,template,context)


def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category)
    return render(request , 'shop/products/list.html', {'category': category,
                                 'categories': categories,
                                 'products': products} )
def product_details(request, id, slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/products/detail.html',{'product':product,'cart_product_form':cart_product_form})