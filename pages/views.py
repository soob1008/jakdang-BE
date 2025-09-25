from rest_framework import generics
from rest_framework.response import Response
from django.conf import settings
from .serializers import PageSerializer

supabase = settings.supabase

# Create your views here.
class PageDetailBySlugView(generics.RetrieveAPIView):
    def get(self, request, slug):
        # Supabase 쿼리
        result = supabase.table("pages").select("*").eq("slug", slug).execute()
        if not result.data:
            return Response({"error": "Page not found"}, status=404)

        page = result.data[0]  # 첫번째 결과
        serializer = PageSerializer(page)
        return Response(serializer.data)