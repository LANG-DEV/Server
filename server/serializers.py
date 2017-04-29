from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from rest_framework import serializers

from server.data_model.request_model import RequestModel
from server.data_model import identity_model


class LangEncoder(DjangoJSONEncoder):
    def default(self, obj):
        print 'LangEncoder: ', obj
        if isinstance(obj, RequestModel):
            return force_text(obj)
        return super(LangEncoder, self).default(obj)

# serialize('json', RequestModel.objects.all(), cls=LangEncoder)

class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = identity_model.IdentityModel
