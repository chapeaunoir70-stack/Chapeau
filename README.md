# API Endpoints

## /captures

### Description
This endpoint handles the capture of events for the application.

### Request
- Method: POST
- URL: `/captures`

### Body
```json
{
  "event_type": "string",
  "data": "object"
}
```

### Response
- Code: 201
- Content: The created capture data.

### Example
```json
{
  "event_type": "user_signup",
  "data": {
    "user_id": "12345"
  }
}
```
