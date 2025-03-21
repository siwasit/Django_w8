from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import Product, ProductComment
from django.shortcuts import render, get_object_or_404

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()  # Retrieve all users
    serializer = UserSerializer(users, many=True)  # Serialize data
    return Response(serializer.data)  # Return JSON response


@api_view(['GET'])
def user_individual(request, username):
    try:
        # Retrieve the user by user_id
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)  # Serialize data for a single user
        return Response(serializer.data)  # Return JSON response
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=404)  # Handle user not found

def product_list(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    # Retrieve the product by its ID or return a 404 if not found
    product = get_object_or_404(Product, id=product_id)
    
    # Pass the product to the template
    return render(request, 'product_detail.html', {'product': product})

def product_comment(request, product_id):
    # Retrieve the product by its ID or return a 404 if not found
    product = get_object_or_404(Product, id=product_id)
    
    # Retrieve the comments related to the product
    comments = ProductComment.objects.filter(product=product)

    # Pass the product and comments to the template
    return render(request, 'product_comment.html', {'product': product, 'comments': comments})


def summarize(request):
    # Get all products
    products = Product.objects.all()
    
    total_amount = 0
    total_buys = 0
    total_comments = 0
    
    for product in products:
        # Summing product amounts
        total_amount += product.product_amount
        
        # Assuming each product has a 'buy_count' field
        total_buys += product.total_buy
        
        # Summing the number of comments
        total_comments += ProductComment.objects.filter(product=product).count()

    context = {
        'total_amount': total_amount,
        'total_buys': total_buys,
        'total_comments': total_comments
    }

    return render(request, 'summarize.html', context)
