from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Country
from .serializers import CountrySerializer
from rest_framework import status
from django.contrib.gis.geos import GEOSGeometry
import json
# Create your views here.

class HomeView(APIView):
	"""
	Home view lists the first 10 countries stored in the database.
	A post request adds a new country to the database.
	"""

	def get(self, request):
		queryset = Country.objects.filter()[:10]
		countries = CountrySerializer(queryset, many=True)
		return Response({
			'msg': 'Welcome',
			'countries': countries.data
			}, status=status.HTTP_200_OK)

	def post(self, request):
		try:
			geometry = request.data['geometry']
			geom_dict = {
				"type": geometry["type"],
				"coordinates": geometry["coordinates"]
			}
			geom = GEOSGeometry(json.dumps(geom_dict))
			country = {
				'admin': request.data["properties"]["ADMIN"],
				'iso_a3': request.data["properties"]["ISO_A3"],
				'geom': geom,
			}
			serializer = CountrySerializer(data=country)
			if serializer.is_valid():
				serializer.save()
				return Response({'msg': 'Country added successfully'}, status=status.HTTP_201_CREATED)
		except:
			return Response({'err': 'Incorrect format'}, status=status.HTTP_400_BAD_REQUEST)


class CountryView(APIView):
	"""
	View used to run read and delete operations on the country table.
	"""
	def get(self, request, name):
		"""
		Get country by name
		"""
		query = Country.objects.filter(admin__contains=name)
		if not query:
			return Response({'err': 'No country with the given name exists'})
		country = CountrySerializer(query, many=True)
		return Response({'country': country.data})

	def delete(self, request, name):
		"""
		Delete country by name
		"""
		query = Country.objects.filter(admin=name)
		if not query:
			return Response({'err': 'No country with the given name exists'})
		elif query.count() != 1:
			return Response({'err': 'No country with the given name exists'})
		country = query[0]
		country.delete()
		return Response({'msg': f'{name} deleted successfully.'})

class IntersectIndiaView(APIView):
	"""
	Return countries that intersect with India
	"""
	def get(self, request):
		india = Country.objects.get(admin='India')
		queryset = Country.objects.filter(geom__intersects=india.geom)
		countries = CountrySerializer(queryset, many=True)

		return Response({'countries': countries.data}, status=status.HTTP_200_OK)