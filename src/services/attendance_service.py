class AttendanceService:
    """Placeholder service for attendance business logic."""

    def __init__(self, repository=None):
        self.repository = repository

    def get_dashboard_data(self):
        return {
            "total_students": 0,
            "total_classes": 0,
            "attendance_rate": 0,
        }
