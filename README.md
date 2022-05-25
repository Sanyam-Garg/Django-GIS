# Django-GIS API
This is a spatial REST API built using Django rest framework and PostgreSQL database with the PostGIS extension.

## Instructions to set up
1. Ensure you have Docker installed.
2. From the root directory of the repository, run the `docker compose up` command to build the images for the web server and postgres database. Wait for the containers to start.
3. Run the `docker ps` command to list the running containers. There should be two: One for the web server, and the other for the database.
4. Enter into a shell in the postgres container with `docker exec -it <container_id> bash` and run the following commands in sequence to install dependencies.
	* apt-get update
	* apt-get install postgis postgresql-14-postgis-3 software-properties-common -y
	* add-apt-repository ppa:ubuntugis/ppa -y
	* apt-get install gdal-bin -y
5. Visit `http://0.0.0.0:8000/api` on your browser to view the API

## API Endpoints
The REST API has three endpoints.
1. `/api/`
	This endpoint has two request methods.
	* GET : A GET request to this endpoint returns the first 10 countries stored in the database in a JSON format.
	* POST: The format of the post request is similar to that of a geojson data file:
	```JSON
	{ "type": "Feature", 
	  "properties": { "ADMIN": "Aruba", "ISO_A3": "ABW" }, 
	  "geometry": { "type": "Polygon", "coordinates": [ [ [ -69.996937628999916, 12.577582098000036 ], [ -69.936390753999945, 12.531724351000051 ], [ -69.924672003999945, 12.519232489000046 ], [ -69.915760870999918, 12.497015692000076 ], [ -69.880197719999842, 12.453558661000045 ], [ -69.876820441999939, 12.427394924000097 ], [ -69.888091600999928, 12.417669989000046 ], [ -69.908802863999938, 12.417792059000107 ], [ -69.930531378999888, 12.425970770000035 ], [ -69.945139126999919, 12.44037506700009 ], [ -69.924672003999945, 12.44037506700009 ], [ -69.924672003999945, 12.447211005000014 ], [ -69.958566860999923, 12.463202216000099 ], [ -70.027658657999922, 12.522935289000088 ], [ -70.048085089999887, 12.531154690000079 ], [ -70.058094855999883, 12.537176825000088 ], [ -70.062408006999874, 12.546820380000057 ], [ -70.060373501999948, 12.556952216000113 ], [ -70.051096157999893, 12.574042059000064 ], [ -70.048736131999931, 12.583726304000024 ], [ -70.052642381999931, 12.600002346000053 ], [ -70.059641079999921, 12.614243882000054 ], [ -70.061105923999975, 12.625392971000068 ], [ -70.048736131999931, 12.632147528000104 ], [ -70.00715084499987, 12.5855166690001 ], [ -69.996937628999916, 12.577582098000036 ] ] ] } 
	}
	```
	After sending a post request with the above JSON data, a country with the Name=Aruba, iso_a3=ABW with a polygon geometry is created.
2. `countries/<str:name>/`
	This endpoint has two request methods.
	* GET : A get request to for example `/countries/Ind` returns a JSON array of all countries whose name contains the string "Ind".
	* DELETE: 
		* A delete request to `/countries/Ind` returns an error message indicating that a country with the name "Ind" does not exist.
		* A delete request to `/countries/India` deletes the country named "India" from the database if found.
3. `query/intersect-india/`
	This endpoint executes a spatial query in the backend and a GET request to this endpoint returns the JSON array of all countries that intersect India. 