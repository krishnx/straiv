# 🏨 PMS Integration Service

This is a Django service that integrates with a mocked Property Management System (PMS) API. It fetches booking data, maps it to an internal format, stores it in a local database, and exposes it via a REST endpoint.

---

## Features

- Fetches bookings from an external (mocked) PMS API
- Maps external data to internal structure
- Stores and returns mapped bookings via a REST API
- Swagger UI documentation
- Unit tested mapping logic

---

## Make commands
```bash
# 1. Run make migrate once before first run to set up DB.
make makemigrations
make migrate

# 2. Run make runserver to launch the Django server.
make run

# 3. Run unit tests
make test

# 4. Run lint
make lint

5. Run make clean to clean up Python cache files.
make clean

6. Install dependencies
make install
```

## Sample cURL commands
```bash
1. GET bookins
curl -X 'GET' \
  'http://localhost:8000/api/integrations/pms/bookings/' \
  -H 'accept: application/json' \
  -H 'X-CSRFTOKEN: aOC913NMG8vt7ekbrAMgytoRrtEsM9RmPcPE9IvmZIU2OzVqRYzUVJ665uJclz8v'

2. POST bookings
curl -X 'POST' \
  'http://localhost:8000/api/integrations/pms/bookings/save/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFTOKEN: aOC913NMG8vt7ekbrAMgytoRrtEsM9RmPcPE9IvmZIU2OzVqRYzUVJ665uJclz8v' \
  -d '{
  "id": "256",
  "guest_name": "Alice",
  "room": "202",
  "from_date": "2025-06-25",
  "to_date": "2025-06-25",
  "misc": {}
}'
```
