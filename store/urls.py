from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('startingpage', views.StartingPageView.as_view(), name="startingpage"),
    path('startingpage/male', views.MalePage.as_view(), name="male"),
    path('startingpage/female', views.FemalePage.as_view(), name="female"),
    path('startingpage/kids', views.KidsPage.as_view(), name="kids"),
    path('startingpage/sports', views.SportsPage.as_view(), name="sports"),
    path('startingpage/male/<int:pk>', views.MaleDetailPage.as_view(), name="maledetail"),
    path('startingpage/female/<int:pk>', views.FemaleDetailPage.as_view(), name="femaledetail"),
    path('startingpage/kids/<int:pk>', views.KidsDetailPage.as_view(), name="kidsdetail"),
    path('startingpage/sports/<int:pk>', views.SportsDetailPage.as_view(), name="sportsdetail"),
    path('startingpage/favourites', views.FavouritePage.as_view(), name="favourite"),
    path('startingpage/add-to-bag', views.AddToBag.as_view(), name="addtobag"),
    path('startingpage/help', views.Help.as_view(), name="help"),
    path('startingpage/contact-us', views.ContactUs.as_view(), name="contact"),
    path('startingpage/bag', views.BagView.as_view(), name="bag"),
    path('startingpage/checkout', views.CheckoutView.as_view(), name="checkout")
]
