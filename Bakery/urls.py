from django.urls import path
from Bakery.Views import views, login, signup, cart

urlpatterns = [
	path('', views.index.as_view(), name='Bakery-index'),
	path('orderhistory/', views.order_history, name='Bakery-order'),
	path('placeorder/', views.place_order, name='Bakery-placeorder'),
	
	path('signup/', signup.Signup.as_view(), name='Bakery-signup'),
	path('login/', login.Login.as_view(), name='Bakery-login'),
	
]