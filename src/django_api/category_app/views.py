from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        return Response (status=HTTP_200_OK, data=[
            {
                'id': '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
                'name': 'Filme',
                'description': 'Filmes em geral',
                'is_active': True
            },
            {
                'id': '6f1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
                'name': 'Séries',
                'description': 'Séries em geral',
                'is_active': True
            }
        ])