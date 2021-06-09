from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import stripe
from stripe import Charge

# Create your views here.
class OrdersPageView(TemplateView):
    template_name = 'purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            # 242 https://docs.djangoproject.com/en/2.2/topics/templates/#django.template.backends.base.Template.render284
            # Chapter 14: Orders with Stripe
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
    )
    return render(request, 'charge.html')