from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.signin, name="login"),
    path('register/',views.register, name="register"),
    path('logout/',views.user_logout, name="logout"),
    path('singlecategory/<category>/',views.singlecategory, name="singlecategory"),
    path('categorydetails/<title>/',views.categorydetails, name="categorydetails"),
    path('contact_us/',views.contact, name="contact"),
    # path('chat/',views.chatbot, name="chat"),
    path('booking/<title>/',views.bookservice, name="booking"),
    path('vendorregistration/',views.vendorregi, name="vendorregistration"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('addservice/',views.addservice, name="addservice"),
    path('allservice/',views.allservice, name="allservice"),
    path('bookinglist/',views.bookinglist, name="bookinglist"),
    path('vendorlogin/',views.vendorsignin, name="vendorlogin"),
    path('about/',views.about, name="about")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
