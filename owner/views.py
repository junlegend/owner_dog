import json
from django.db.models.fields import EmailField
from django.http import JsonResponse
from django.views import View
from owner.models import Owner, Dog


class OwnerView(View):
    #:8000/owners
    def get(self, request):
        owners = Owner.objects.all()
        result = []
        for owner in owners:
            result.append({"name": owner.name, "email": owner.email, "age": owner.age})
        return JsonResponse({"result": result}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data["name"], email=data["email"], age=data["age"])

        return JsonResponse({"massage": "SUCCESS"}, status=201)


class DogView(View):
    # :8000/dogs
    # :8000/owners/dogs
    def get(self, request):
        dogs = Dog.objects.all()
        result = []
        for dog in dogs:
            result.append({"name": dog.name, "age": dog.age, "owner": dog.owner_id})
        return JsonResponse({"result": result}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            name=data["name"], age=data["age"], owner_id=data["owner_id"]
        )

        return JsonResponse({"massage": "SUCCESS"}, status=201)
