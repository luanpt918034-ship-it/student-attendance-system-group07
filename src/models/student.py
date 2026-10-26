from dataclasses import dataclass


@dataclass
class Student:
    student_id: str
    full_name: str
    email: str | None = None


@dataclass
class AttendanceRecord:
    student_id: str
    class_id: str
    date: str
    status: str = "present"
