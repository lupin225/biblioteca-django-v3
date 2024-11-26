from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from core.views import ColecaoListCreate, ColecaoDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Rotas para Livros
    path('livros/', views.LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),

    # Rotas para Categorias
    path('categorias/', views.CategoriaList.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),

    # Rotas para Autores
    path('autores/', views.AutorList.as_view(), name='autores-list'),
    path('autores/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),

    # Endpoint para gerar o schema OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Redoc UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    path('api/colecoes/', ColecaoListCreate.as_view(), name='colecao-list-create'),
    path('api/colecoes/<int:pk>/', ColecaoDetail.as_view(), name='colecao-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]