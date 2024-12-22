from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API de Recrutement",
        default_version='1',
        description="Documentation de l'API de gestion des candidats et recruteurs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="halilkenza2005@gmail.com"),
        license=openapi.License(name="Licence MIT"),
    ),
    public=True,
)