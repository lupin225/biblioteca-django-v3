from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Colecao

class ColecaoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.force_authenticate(user=self.user)
        self.colecao_data = {"nome": "Minha Coleção", "descricao": "Descrição"}

    def test_criar_colecao(self):
        response = self.client.post("/api/colecoes/", self.colecao_data)
        print(response.data)  # Para verificar erros
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_editar_colecao(self):
        colecao = Colecao.objects.create(nome="Coleção 1", colecionador=self.user)
        response = self.client.patch(f"/api/colecoes/{colecao.id}/", {"descricao": "Nova descrição"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permicao_editar(self):
        outro_usuario = User.objects.create_user(username="outro", password="senha")
        colecao = Colecao.objects.create(nome="Coleção 2", colecionador=outro_usuario)
        response = self.client.patch(f"/api/colecoes/{colecao.id}/", {"descricao": "Teste"})
        print(response.data)  # Para verificar erros
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
