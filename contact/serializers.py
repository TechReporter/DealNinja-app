from rest_framework import serializers
from . import models


class ContactSerializer(serializers.ModelSerializer):
    notes = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Contact
        fields = (
            'id', 'f_name', 'l_name', 'status', 'title', 'email', 'mobile', 'office_number', 'company', 'corporate_ph',
            'address_1', 'address_2', 'postal_code', 'website', 'emp_count', 'yearly_revenue','notes')
    # fields = "__all__"
