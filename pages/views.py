from rest_framework import generics
from .models import Page
from .serializers import PageSerializer

# slug로 1개 페이지 조회
class PageDetailBySlugView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = "slug"