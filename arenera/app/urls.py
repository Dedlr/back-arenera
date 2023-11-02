from rest_framework.routers import DefaultRouter
from app.views.client import ClientViewSet
from app.views.base import MeasureUnitViewSet
from app.views.product import ProductViewSet
from app.views.user import UserViewSet
from app.views.sale import SaleViewSet

router = DefaultRouter()

router.register(r'clients',ClientViewSet,basename = 'clients')
router.register(r'measure_unit',MeasureUnitViewSet,basename = 'measure_unit')
router.register(r'products',ProductViewSet,basename = 'products')
router.register(r'users', UserViewSet, basename="users")
router.register(r'sales', SaleViewSet, basename="sales")


urlpatterns = router.urls