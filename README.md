# API Authentication

This repository demonstrates how to implement authentication and permissions for APIs using Django REST Framework (DRF). The focus is on two primary authentication methods: **Session Authentication** and **Basic Authentication**, as well as how to use **Permission Classes** to control API access.

## Authentication Methods

### 1. Session Authentication

- **Session Authentication** uses Django's built-in session framework.
- When a user logs in through Django’s login view, a session is created and maintained via cookies.
- DRF checks for a valid session ID in the incoming request’s cookies to authenticate the user.
- Commonly used for web clients (browsers) that can handle cookies.

**Usage Example:**
```python
from rest_framework.authentication import SessionAuthentication
```

### 2. Basic Authentication

- **Basic Authentication** uses the HTTP Basic Auth standard.
- The client sends the username and password with each request encoded in the `Authorization` header.
- DRF decodes the credentials and authenticates the user.
- Suitable for testing and scripts, but not recommended for production as credentials are sent with every request.

**Usage Example:**
```python
from rest_framework.authentication import BasicAuthentication
```

## Permission Classes

Permission classes determine whether a user is authorized to access an API endpoint after authentication.

- DRF provides built-in permission classes like `IsAuthenticated`, `IsAdminUser`, and `AllowAny`.
- You can also create custom permission classes for more granular control.

**Example: Restricting API access to authenticated users**
```python
from rest_framework.permissions import IsAuthenticated

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Your logic here
        return Response({"message": "You are authenticated"})
```

## Summary

- Use **SessionAuthentication** for browser-based clients.
- Use **BasicAuthentication** for simple scripts or testing.
- Combine authentication with **Permission Classes** to control API access.

For more details, refer to the [Django REST Framework Authentication Docs](https://www.django-rest-framework.org/api-guide/authentication/) and [Permissions Docs](https://www.django-rest-framework.org/api-guide/permissions/).
