from petstagram.pets.models import Pet


def get_pet_by_username_and_slug(username, pet_slug):
    # TODO: fix `username` when auth
    return Pet.objects.get(slug=pet_slug)