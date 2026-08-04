import os
import django
import random
from faker import Faker

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_management.settings")
django.setup()

from tasks.models import employees, project, Task, TaskDetail


def populate_db():
    fake = Faker()

    # Create 3 Projects
    projects = [
        project.objects.create(
            project_name=fake.bs().capitalize(),
            description=fake.paragraph(),
            start_date=fake.date_this_year(),
        )
        for _ in range(3)
    ]

    print(f"Created {len(projects)} projects.")

    # Create 10 Employees
    employee_list = [
        employees.objects.create(
            name=fake.name(),
            email=fake.unique.email(),
        )
        for _ in range(10)
    ]

    print(f"Created {len(employee_list)} employees.")

    # Create ONLY 10 Tasks
    tasks = []

    for _ in range(10):
        task = Task.objects.create(
            project=random.choice(projects),
            title=fake.sentence(nb_words=4),
            description=fake.paragraph(),
            due_date=fake.date_this_year(),
            status=random.choice(
                ["PENDING", "IN_PROGRESS", "COMPLETED"]
            ),
            is_completed=random.choice([True, False]),
        )

        task.assign_to.set(
            random.sample(employee_list, random.randint(1, 3))
        )

        tasks.append(task)

    print(f"Created {len(tasks)} tasks.")

    # Task Details
    for task in tasks:
        TaskDetail.objects.create(
            task=task,
            priority=random.choice(["H", "M", "L"]),
            notes=fake.paragraph(),
        )

    print("Database populated successfully!")


if __name__ == "__main__":
    populate_db()