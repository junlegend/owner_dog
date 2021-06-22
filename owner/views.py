import json
from django.db.models.fields import EmailField
from django.http import JsonResponse
from django.views import View
from owner.models import Owner, Dog


class OwnerView(View):
    def get(self, request):
        owners = Owner.objects.all()
        result = []
        for owner in owners:
            dogs = owner.dog_set.all()
            dogs_list = []
            for dog in dogs:
                dogs_list.append({"1.dog_name": dog.name, "2.dog_age": dog.age})

            result.append(
                {
                    "1.name": owner.name,
                    "2.email": owner.email,
                    "3.age": owner.age,
                    "4.dog_list": dogs_list,
                }
            )
        return JsonResponse({"result": result}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data["name"], email=data["email"], age=data["age"])

        return JsonResponse({"massage": "SUCCESS"}, status=201)


class DogView(View):
    def get(self, request):
        dogs = Dog.objects.all()
        result = []
        for dog in dogs:
            result.append(
                {
                    "1.name": dog.name,
                    "2.age": dog.age,
                    "3.owner_name": dog.owner.name,
                }
            )
        return JsonResponse({"result": result}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            name=data["name"],
            age=data["age"],
            owner_id=data["owner_id"],
        )

        return JsonResponse({"massage": "SUCCESS"}, status=201)
