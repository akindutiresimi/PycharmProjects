
class Student:
        students = {
            "jpaul": {                                   #
                "name": "John Paul",
                "age": 22,
                "courses": {"Math", "Physics"},
                "address": {"city": "...", "zip": "..."}
            },
        }

    OFFERED_COURSES = (
        "Math", "Physics", "Computer Science", "Biology", "Chemistry",
        "Statistics", "English", "Economics", "History", "Philosophy",
        "Sociology", "Political Science", "Geography", "Psychology", "Art",
        "Music", "Engineering", "Law", "Medicine", "Business",
    )

    def _get_student(students, username):
        if username not in students:
            raise KeyError(f"Student '{username}' does not exist")
        return students[username]

    def _validate_text(value, label):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{label} cannot be empty")
        return value.strip()

    def _validate_age(age):
        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            raise ValueError("Age must be a positive whole number")
        return age

    def _validate_offered(course):
        if course not in OFFERED_COURSES:
            raise ValueError(f"'{course}' is not offered by the department")


    def create_student(students, username, name, age, courses, city, zip_code):
        username = _validate_text(username, "Username")
        if username in students:
            raise ValueError(f"Username '{username}' is already taken")

        name = _validate_text(name, "Name")
        age = _validate_age(age)
        city = _validate_text(city, "City")
        zip_code = _validate_text(zip_code, "Zip code")

        course_set = set(courses)
        for course in course_set:
            _validate_offered(course)

        students[username] = {
            "name": name,
            "age": age,
            "courses": course_set,
            "address": {"city": city, "zip": zip_code},
        }


    def display_student_record(students, username):
        student = _get_student(students, username)
        courses = ", ".join(sorted(student["courses"])) or "none"
        return (
            "Username: {username}"
            f"Name:     {student['name']}"
            f"Age:      {student['age']}"
            f"Courses:  {courses}"
            f"City:     {student['address']['city']}"
            f"Zip code: {student['address']['zip']}"
        )


    def display_student_courses(students, username):
        student = _get_student(students, username)
        if not student["courses"]:
            return f"{username} has no courses yet."
        return f"Courses of {username}: " + ", ".join(sorted(student["courses"]))


    def display_zip_code(students, username):
        return _get_student(students, username)["address"]["zip"]


    def display_city(students, username):
        return _get_student(students, username)["address"]["city"]


    def add_course(students, username, course):
        student = _get_student(students, username)
        _validate_offered(course)
        if course in student["courses"]:
            raise ValueError(f"Student already takes '{course}'")
        student["courses"].add(course)

    def remove_course(students, username, course):
        student = _get_student(students, username)
        if course not in student["courses"]:
            raise ValueError(f"Student is not enrolled in '{course}'")
        student["courses"].remove(course)

    def update_course(students, username, old_course, new_course):
        student = _get_student(students, username)
        if old_course not in student["courses"]:
            raise ValueError(f"Student is not enrolled in '{old_course}'")
        _validate_offered(new_course)
        if new_course in student["courses"]:
            raise ValueError(f"Student already takes '{new_course}'")
        student["courses"].remove(old_course)
        student["courses"].add(new_course)

    def update_student(students, username, name=None, age=None, city=None, zip_code=None):
        student = _get_student(students, username)
        if all(value is None for value in (name, age, city, zip_code)):
            raise ValueError("Give at least one field to update")

        new_name = _validate_text(name, "Name") if name is not None else None
        new_age = _validate_age(age) if age is not None else None
        new_city = _validate_text(city, "City") if city is not None else None
        new_zip = _validate_text(zip_code, "Zip code") if zip_code is not None else None

        if new_name is not None:
            student["name"] = new_name
        if new_age is not None:
            student["age"] = new_age
        if new_city is not None:
            student["address"]["city"] = new_city
        if new_zip is not None:
            student["address"]["zip"] = new_zip

    def count_students(students):
        return len(students)


    if __name__ == "__main__":
        main()