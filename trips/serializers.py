from rest_framework import serializers
from trips.models import User, Overview, Segment
import datetime

# http://www.django-rest-framework.org/tutorial/1-serialization/


class UserSerializer(serializers.ModelSerializer):

    # overviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Overview.objects.all())

    # Because 'overviews' is a reverse relationship on the User model,
    # it will not be included by default when using the ModelSerializer class,
    # so we needed to add an explicit field for it.

    class Meta:
        model = User
        fields = ('id', 'username')

        # fields = ('id', 'username', 'overviews')


class OverviewSerializer(serializers.ModelSerializer):

    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Overview
        # fields = ('title', 'length', 'season', 'activity_type', 'pub_date', 'owner')
        fields = ('title', 'length', 'season', 'activity_type', 'pub_date')


class SegmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Segment
        fields = ('overview_id', 'province', 'region', 'country')

