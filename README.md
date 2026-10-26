# student-attendance-system-group07
Student Attendance System project for Group 07.

## Project structure

```text
src/
├── controllers/
├── services/
├── repositories/
├── models/
├── views/
│   ├── templates/
│   └── static/
├── config.py
└── __init__.py
tests/
app.py
requirements.txt
.env.example
```

## Quick start

1. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Copy environment variables
   ```bash
   cp .env.example .env
   ```
4. Run the app
   ```bash
   python app.py
   ```
5. Open in browser
   ```text
   http://127.0.0.1:5000/
   ```

## Notes

This scaffold follows a layered architecture:
- Controller handles routes
- Service contains business logic
- Repository handles data access
- Model defines entities
- Views render templates and static assets
