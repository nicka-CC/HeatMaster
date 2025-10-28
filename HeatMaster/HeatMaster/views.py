from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CalculatePriceForm, CustomUserCreationForm, CustomAuthenticationForm, CommentBlogForm, BlogForm, \
    ImageBlogForm, ThermostatCommentForm
from .models import Thermostats, Blog, CommentBlog, ImageBlog, Thermostat, ThermostatImages, Applications, HeatedMats, Produce, \
    Cart, CartItem, Order, OrderItem, ThermostatComment
from .forms import ApplicationForm
from django.core.paginator import Paginator
from django.db.models import Q, Count


def home(request):
    thermostats = Thermostats.objects.all()
    return render(request, 'pages/home.html', {'thermostats': thermostats})
def thermoregulator(request):
    thermostats = Thermostats.objects.all()
    return render(request, 'pages/thermoregulator.html', {'thermostats': thermostats})

def about(request):
    return render(request, 'pages/about.html')
def calculate_price(request):
    if request.method == "POST":
        form = CalculatePriceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/calculate_price.html', context={'form_data': form.cleaned_data})
    else:
        form = CalculatePriceForm()
    return render(request, 'pages/calculate_price.html',{'form':form})

def signUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/signUp.html', {'form': form})

def signIn(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'pages/signIn.html', {'form': form})
def blog(request):
    blogs = Blog.objects.prefetch_related("blod").all()
    return render(request, "pages/blog.html", {"blogs": blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog.objects.prefetch_related("blod"), id=blog_id)
    comments = CommentBlog.objects.filter(blog=blog).order_by('-date')

    if request.method == 'POST':
        form = CommentBlogForm(request.POST, user=request.user, blog=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = CommentBlogForm(user=request.user, blog=blog)

    return render(request, 'pages/blog_detail.html', {
        'blog': blog,
        'form': form,
        'comments': comments
    })
def create_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        image_form = ImageBlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_instance = blog_form.save()
            files = request.FILES.getlist('image_1')
            for file in files:
                image_instance = ImageBlog(image=file, blog=blog_instance, status='header')
                image_instance.save()
            return redirect('blog_detail', blog_id=blog_instance.id)
    else:
        blog_form = BlogForm()
        image_form = ImageBlogForm()
    return render(request, 'pages/create_blog.html', {
        'blog_form': blog_form,
        'image_form': image_form
    })

def videos(request):
    return render(request, 'pages/videos.html')


def heated_mats(request):
    # simple content page with application form (create Applications record)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.status = 'new'
            app.save()
            return render(request, 'pages/heated_mats.html', {'form': ApplicationForm(), 'success': True})
    else:
        form = ApplicationForm()

    mats = HeatedMats.objects.all()
    return render(request, 'pages/heated_mats.html', {'form': form, 'mats': mats})


def contacts(request):
    # Contact page with Yandex map and short contact form (reuse ApplicationForm)
    submitted = False
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.status = 'new'
            app.save()
            submitted = True
            form = ApplicationForm()
    else:
        form = ApplicationForm()

    return render(request, 'pages/contacts.html', {'form': form, 'submitted': submitted})

def aquastrage(request):
    # Contact page with Yandex map and short contact form (reuse ApplicationForm)
    submitted = False
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.status = 'new'
            app.save()
            submitted = True
            form = ApplicationForm()
    else:
        form = ApplicationForm()

    return render(request, 'pages/aquastrage.html', {'form': form, 'submitted': submitted})

def cable(request):
    # Contact page with Yandex map and short contact form (reuse ApplicationForm)
    submitted = False
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.status = 'new'
            app.save()
            submitted = True
            form = ApplicationForm()
    else:
        form = ApplicationForm()

    return render(request, 'pages/cable.html', {'form': form, 'submitted': submitted})

def infraredCable(request):
    # Contact page with Yandex map and short contact form (reuse ApplicationForm)
    submitted = False
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.status = 'new'
            app.save()
            submitted = True
            form = ApplicationForm()
    else:
        form = ApplicationForm()

    return render(request, 'pages/infrared-cable.html', {'form': form, 'submitted': submitted})

def pruityOfSnowmelt(request):
    # Contact page with Yandex map and short contact form (reuse ApplicationForm)
    submitted = False
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.status = 'new'
            app.save()
            submitted = True
            form = ApplicationForm()
    else:
        form = ApplicationForm()

    return render(request, 'pages/pruity-of-snowmelt.html', {'form': form, 'submitted': submitted})

def thinLaminateCable(request):
    # Contact page with Yandex map and short contact form (reuse ApplicationForm)
    submitted = False
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.status = 'new'
            app.save()
            submitted = True
            form = ApplicationForm()
    else:
        form = ApplicationForm()

    return render(request, 'pages/thin-laminate-cable.html', {'form': form, 'submitted': submitted})

def thinCable(request):
    # Contact page with Yandex map and short contact form (reuse ApplicationForm)
    submitted = False
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.status = 'new'
            app.save()
            submitted = True
            form = ApplicationForm()
    else:
        form = ApplicationForm()

    return render(request, 'pages/thin-cable.html', {'form': form, 'submitted': submitted})



def delivery_payment(request):
    # static page describing delivery and payment options
    return render(request, 'pages/delivery_payment.html')


def cooperation(request):
    # static cooperation/partners page
    return render(request, 'pages/cooperation.html')


def manufacturers(request):
    producers = Produce.objects.all()
    return render(request, 'pages/manufacturers.html', {'producers': producers})


def thermostat_list(request, type_id=None):
    """List of thermostats with multiple sidebar filters and pagination.

    URL can provide `type_id` as path param (via thermostats/type/<id>/) or GET param `type_id`.
    Sidebar includes manufacturers and countries with counts and price range.
    """
    # show only items with positive stock
    qs = Thermostat.objects.filter(available__gt=0)

    # allow type in path or GET
    type_param = type_id or request.GET.get('type_id')
    if type_param:
        try:
            type_int = int(type_param)
            qs = qs.filter(thermostats_id=type_int)
        except (ValueError, TypeError):
            type_int = None
    else:
        type_int = None

    # simple search
    q = request.GET.get('q')
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(manufacturer__icontains=q) | Q(model__icontains=q))

    # sidebar filters: manufacturer and country with counts
    manufacturers = qs.values('manufacturer').order_by('manufacturer')
    manufacturer_counts = qs.values('manufacturer').annotate(count=Count('id')).order_by('-count')

    countries_counts = qs.values('country_manufacturer').annotate(count=Count('id')).order_by('-count')

    # price range present in current qs (before price filtering)
    prices = qs.exclude(price__isnull=True).values_list('price', flat=True)
    if prices:
        price_min = int(min(prices))
        price_max = int(max(prices))
    else:
        price_min = 0
        price_max = 0

    # Apply GET filters: manufacturers (comma separated), countries (comma separated), price_min/price_max
    manufacturers_filter = request.GET.get('m')
    if manufacturers_filter:
        manu_list = [x for x in manufacturers_filter.split(',') if x]
        qs = qs.filter(manufacturer__in=manu_list)

    countries_filter = request.GET.get('c')
    if countries_filter:
        country_list = [x for x in countries_filter.split(',') if x]
        qs = qs.filter(country_manufacturer__in=country_list)

    try:
        price_min_filter = int(request.GET.get('price_min')) if request.GET.get('price_min') else None
        price_max_filter = int(request.GET.get('price_max')) if request.GET.get('price_max') else None
    except ValueError:
        price_min_filter = price_max_filter = None

    if price_min_filter is not None:
        qs = qs.filter(price__gte=price_min_filter)
    if price_max_filter is not None:
        qs = qs.filter(price__lte=price_max_filter)

    # pagination
    page_size = 12
    paginator = Paginator(qs.order_by('id'), page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    types = Thermostats.objects.all()

    # preserve current GET params except page (for pagination links)
    params = request.GET.copy()
    if 'page' in params:
        params.pop('page')
    current_get = params.urlencode()

    return render(request, 'pages/thermostat_list.html', {
        'page_obj': page_obj,
        'types': types,
        'selected_type': type_int,
        'q': q or '',
        'manufacturer_counts': manufacturer_counts,
        'countries_counts': countries_counts,
        'price_min': price_min,
        'price_max': price_max,
        'current_get': current_get,
    })


def thermostat_detail(request, pk):
    thermostat = get_object_or_404(Thermostat, pk=pk)
    images = ThermostatImages.objects.filter(thermostat_image=thermostat)
    comments = ThermostatComment.objects.filter(thermostat=thermostat).select_related('user').order_by('-created_at')

    form = None
    if request.user.is_authenticated:
        form = ThermostatCommentForm()

    return render(request, 'pages/thermostat_detail.html', {
        'thermostat': thermostat,
        'images': images,
        'comments': comments,
        'comment_form': form,
    })


def create_comment(request, thermostat_id):
    if not request.user.is_authenticated:
        return redirect('signIn')
    thermostat = get_object_or_404(Thermostat, id=thermostat_id)
    if request.method == 'POST':
        form = ThermostatCommentForm(request.POST)
        if form.is_valid():
            ThermostatComment.objects.create(
                thermostat=thermostat,
                user=request.user,
                text=form.cleaned_data['text'],
                rating=form.cleaned_data['rating']
            )
    return redirect('thermostat_detail', pk=thermostat.id)


def edit_comment(request, comment_id):
    comment = get_object_or_404(ThermostatComment, id=comment_id)
    if not request.user.is_authenticated or (request.user != comment.user and not request.user.is_staff):
        return redirect('thermostat_detail', pk=comment.thermostat.id)
    if request.method == 'POST':
        form = ThermostatCommentForm(request.POST)
        if form.is_valid():
            comment.text = form.cleaned_data['text']
            comment.rating = form.cleaned_data['rating']
            comment.save()
            return redirect('thermostat_detail', pk=comment.thermostat.id)
    return redirect('thermostat_detail', pk=comment.thermostat.id)


def delete_comment(request, comment_id):
    comment = get_object_or_404(ThermostatComment, id=comment_id)
    if request.user.is_authenticated and (request.user == comment.user or request.user.is_staff):
        thermostat_id = comment.thermostat.id
        comment.delete()
        return redirect('thermostat_detail', pk=thermostat_id)
    return redirect('thermostat_detail', pk=comment.thermostat.id)


def my_orders(request):
    if not request.user.is_authenticated:
        return redirect('signIn')
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'pages/my_orders.html', {'orders': orders})


# --- Cart and checkout flows ---
def _get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


def add_to_cart(request, thermostat_id):
    if not request.user.is_authenticated:
        return redirect('signIn')

    thermostat = get_object_or_404(Thermostat, id=thermostat_id)
    quantity = 1
    try:
        quantity = int(request.POST.get('quantity', '1'))
    except ValueError:
        quantity = 1
    if quantity < 1:
        quantity = 1

    cart = _get_or_create_cart(request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, thermostat=thermostat)
    new_qty = item.quantity + quantity if not created else quantity
    # clamp by stock
    new_qty = min(new_qty, max(0, thermostat.available))
    item.quantity = new_qty
    item.save()
    return redirect('cart_view')


def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('signIn')
    cart = _get_or_create_cart(request.user)
    return render(request, 'pages/cart.html', {'cart': cart})


def update_cart_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect('signIn')
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    try:
        qty = int(request.POST.get('quantity', '1'))
    except ValueError:
        qty = 1
    qty = max(1, qty)
    qty = min(qty, max(0, item.thermostat.available))
    item.quantity = qty
    item.save()
    return redirect('cart_view')


def remove_cart_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect('signIn')
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('cart_view')


def checkout(request):
    if not request.user.is_authenticated:
        return redirect('signIn')
    cart = _get_or_create_cart(request.user)
    if request.method == 'POST':
        address = request.POST.get('shipping_address', '')
        comment = request.POST.get('comment', '')

        if cart.items.count() == 0:
            return redirect('cart_view')

        order = Order.objects.create(user=request.user, shipping_address=address, comment=comment, status=Order.STATUS_PAID)

        total = 0
        for item in cart.items.select_related('thermostat').all():
            if item.quantity <= 0:
                continue
            # ensure stock available
            if item.thermostat.available < item.quantity:
                # clip to available
                qty = max(0, item.thermostat.available)
            else:
                qty = item.quantity
            if qty == 0:
                continue
            OrderItem.objects.create(order=order, thermostat=item.thermostat, quantity=qty,
                                     price_at_purchase=item.thermostat.price)
            total += item.thermostat.price * qty
            # decrement stock
            item.thermostat.available = max(0, item.thermostat.available - qty)
            item.thermostat.save(update_fields=['available'])
        order.total_amount = total
        order.save(update_fields=['total_amount'])
        # clear cart
        cart.items.all().delete()
        return render(request, 'pages/order_success.html', {'order': order})

    return render(request, 'pages/checkout.html', {'cart': cart})