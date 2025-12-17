from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, PeriodSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Period


class PeriodBaseView(generics.GenericAPIView):
    """Base view for Period operations. Filters to user-owned periods only."""
    serializer_class = PeriodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return periods owned by the authenticated user."""
        return Period.objects.filter(owner=self.request.user)


class PeriodlistCreate(PeriodBaseView, generics.ListCreateAPIView):
    """List user's periods (GET) or create a new period (POST)."""

    def perform_create(self, serializer):
        """Assign the authenticated user as the period owner."""
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        else:
            print(serializer.errors)


class PeriodDelete(PeriodBaseView, generics.DestroyAPIView):
    """Delete a user's period (DELETE)."""
    pass


class CreateUserView(generics.CreateAPIView):
    """Register a new user (POST). No authentication required."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
