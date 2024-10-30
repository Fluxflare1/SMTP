# Trip Scheduling API Documentation

## Endpoints

- **POST /api/trips/**: Create a new trip.
  - Permissions: Admin, Dispatcher
  - Validations:
    - Vehicle and driver availability
    - Origin and destination required

- **PUT /api/trips/{id}/**: Update an existing trip.
  - Permissions: Admin, Dispatcher

## Error Responses

- **400 Bad Request**: Validation errors such as overlapping trips, missing origin/destination.
