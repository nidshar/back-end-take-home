
from django.http import HttpResponse
from django.views import View
from .models import Route, Airline, Airport

class ShortestPathView(View):

    def get(self, request):
        source = request.GET.get("source")
        destination = request.GET.get("destination")
        if source and destination:
            try:
                Airport.objects.get(code=source)
            except Airport.DoesNotExist:
                return HttpResponse("Invalid Origin")
            
            try:
                Airport.objects.get(code=destination)
            except Airport.DoesNotExist:
                return HttpResponse("Invalid Destination")
            path = find_path([source],source,destination)
            if path:
                result = ""
                for code in path[:-1]:
                    result += code + " -> "
                result += path[-1]
                return HttpResponse(result)
            return HttpResponse("No Route")
        return HttpResponse("Please provide source and destination")

# returns the path from source to destination 
def find_path(path,source,destination):
    routes = Route.objects.filter(origin__code=source)
    for route in routes:
        if route.destination.code in path:
            continue
        path.append(route.destination.code)
        if route.destination.code == destination:
            return path
        else:
            return find_path(path,route.destination.code,destination)
    return []