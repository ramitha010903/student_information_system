from setuptools import setup, find_packages

setup(
    name="Student_Management_System",
    version="1.0.0",
    description="A comprehensive Student Management System for managing students, courses, enrollments, teachers, and payments.",
    author="Sanjana",
    author_email="sanjana-email@example.com",
    packages=find_packages(),  # Automatically find packages within your project
    install_requires=[
        "pyodbc",  # For database connectivity
    ],
)
