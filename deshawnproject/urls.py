from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from deshawnapi.views import WalkerView, CityView, DogView

router = routers.DefaultRouter(trailing_slash=False)
# To add routes: This route covers all CRUD and custom action routes
# By registering a route, the app now knows to route all requests coming to /walkers to the WalkerView
# The third argument is the routes 'basename' this is used for error messages
router.register(r'walkers', WalkerView, 'walker')

# TODO: Register the routes for the dog and city view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
