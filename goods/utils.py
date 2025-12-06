from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id = int(query))
    keyword = [word for word in query.split() if len(word) > 2]

    q_objects = Q()
    for token in keyword:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)
    return Products.objects.filter(q_objects)