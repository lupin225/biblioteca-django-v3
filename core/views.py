from rest_framework import generics, filters, permissions
from django_filters import rest_framework as django_filters
from .models import Livro, Categoria, Autor, Colecao
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer, ColecaoSerializer
from .custom_permissions import IsColecionador


# Filtro personalizado para Livro
class LivroFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(field_name='titulo', lookup_expr='icontains')  # Busca por título (case-insensitive)
    autor = django_filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')  # Busca por nome do autor
    categoria = django_filters.AllValuesFilter(field_name='categoria__nome')  # Filtra por nome da categoria

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']

# View para listar e criar Livros com paginação, busca, ordenação e filtros
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter  # Filtro personalizado para Livro
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, django_filters.DjangoFilterBackend]
    search_fields = ['^titulo', '^autor__nome', '^categoria__nome']  # Busca pelo início do nome (^)
    ordering_fields = ['titulo', 'autor__nome', 'categoria__nome', 'publicado_em']  # Ordenação por esses campos
    ordering = ['titulo']  # Ordenação padrão por título

# View para detalhes, atualização e exclusão de Livros
class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# Filtro personalizado para Categoria
class CategoriaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='startswith')  # Busca pelo início do nome

    class Meta:
        model = Categoria
        fields = ['nome']

# View para listar e criar Categorias com paginação, busca, ordenação e filtros
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter  # Filtro personalizado para Categoria
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, django_filters.DjangoFilterBackend]
    search_fields = ['^nome']  # Busca pelo início do nome (^)
    ordering_fields = ['nome']  # Ordenação por nome
    ordering = ['nome']  # Ordenação padrão por nome

# View para detalhes, atualização e exclusão de Categorias
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Filtro personalizado para Autor
class AutorFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='startswith')  # Busca pelo início do nome

    class Meta:
        model = Autor
        fields = ['nome']

# View para listar e criar Autores com paginação, busca, ordenação e filtros
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFilter  # Filtro personalizado para Autor
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, django_filters.DjangoFilterBackend]
    search_fields = ['^nome']  # Busca pelo início do nome (^)
    ordering_fields = ['nome']  # Ordenação por nome
    ordering = ['nome']  # Ordenação padrão por nome

# View para detalhes, atualização e exclusão de Autores
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ColecaoListCreate(generics.ListCreateAPIView):
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
    
        return Colecao.objects.filter(colecionador=self.request.user)

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)


class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated, IsColecionador]

    def get_queryset(self):
        
        return Colecao.objects.filter(colecionador=self.request.user)
