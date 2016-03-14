from rest_framework import generics

from trips.models import Overview, Segment
from trips.serializers import OverviewSerializer, SegmentSerializer
from rest_framework import permissions


# class UserList(generics.ListCreateAPIView):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class OverviewList(generics.ListCreateAPIView):
    """
    List all code overviews, or create a new overview.
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer

    """
    Right now, if we created a code snippet, there'd be no way of associating the user that created the snippet,
    with the snippet instance. The user isn't sent as part of the serialized representation,
    but is instead a property of the incoming request.

    The way we deal with that is by overriding a .perform_create() method on our snippet views,
    that allows us to modify how the instance save is managed,
    and handle any information that is implicit in the incoming request or requested URL.
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OverviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code overview.
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer


class SegmentList(generics.ListCreateAPIView):
    """
    List all code segments, or create a new segment.
    """

    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer


class SegmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code segment.
    """

    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer


