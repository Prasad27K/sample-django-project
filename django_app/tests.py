from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django_app.models import Languages

from django_app.views import LanguagesViewSet
# Create your tests here.
class LanguagesViewSetTest(TestCase):
    def setUp(self):
        Languages.objects.create(id=15, name="Prasad")

    def test_languages_viewset(self):
        factory = APIRequestFactory()
        view = LanguagesViewSet.as_view({'get': 'list'})
        request = factory.get("languages-details")
        print(request)
        response = view(request)
        response_data = dict(response.data[0])
        resp = "Prasad"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["name"], resp)

        