from django.shortcuts import render,redirect
from .forms import AddProduct,CreateUserForm
from . models import Product,Sale
# from django.models import Q

# Create your views here.
def registerPage(request):
	form=CreateUserForm()
	context={'form':form}
	return render(request,'register.html',context)

def loginPage(request):
	context={}
	return render(request,'login.html',context)



def index(request):
	form=AddProduct
	content={'form':form}
	return render(request,'index.html',content)

def testCrispy(request):
	form=AddProduct
	context={'form:form'}
	return render(request,'AddProduct.html',content)


def addProduct(request):
	form=AddProduct
	# if request.method=='POST':
	# 	form=AddProduct(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	context={'form':form}		
	return render(request,'addproduct.html',context)

def tables(request):
	products=Product.objects.all()
	context={
	    'products':products
	}
	return render(request,'tables.html',context)


def sellView(request,pk):
	product=Product.objects.get(id=pk)
	product_count=Product.objects.filter(name=product.name).count()
	context={'product':product,
             'product_count':product_count

	}
	return render(request,'sell.html',context)

def sellP(request,pk):
	product=Product.objects.get(id=pk)
	product.selling_price=400
	product.status='SOLD'
	product.save()
	
	return redirect('tables')

#sales view
def sales(request):
	q=request.GET.get('q') if request.GET.get('q') !=None else ''
	sales=Sale.objects.filter(
		Q(product__created__icontains=q)
		)
	context={}
	return render(request,'sales.html',context)
	





