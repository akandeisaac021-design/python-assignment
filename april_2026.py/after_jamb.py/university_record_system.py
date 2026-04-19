# University Record System

# Dictionary to hold all student records
students = {}

# Department courses (unchangeable list)
department_courses = {
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business"
}

# Function to create a new student record
def create_student(username, name, age, courses, city, zip_code):
    students[username] = {
        "name": name,
        "age": age,
        "courses": set(courses),
        "address": {"city": city, "zip": zip_code}
    }

# 1. Display a student record
def display_student(username):
    return students.get(username, "Student not found")

# 2. Display all courses for a student
def display_courses(username):
    return students[username]["courses"]

# 3. Display only the zip code
def display_zip(username):
    return students[username]["address"]["zip"]

# 4. Display only the city
def display_city(username):
    return students[username]["address"]["city"]

# 5. Add a new course with validation
def add_course(username, course):
    if course in department_courses and course not in students[username]["courses"]:
        students[username]["courses"].add(course)
        return f"{course} added successfully."
    return "Invalid or duplicate course."

# 6. Remove or update a course
def remove_course(username, course):
    students[username]["courses"].discard(course)

def update_course(username, old_course, new_course):
    if old_course in students[username]["courses"]:
        students[username]["courses"].remove(old_course)
        add_course(username, new_course)

# 7. Update student fields
def update_student(username, name=None, age=None, city=None, zip_code=None):
    if name: students[username]["name"] = name
    if age: students[username]["age"] = age
    if city: students[username]["address"]["city"] = city
    if zip_code: students[username]["address"]["zip"] = zip_code

# 8. Display total number of students
def total_students():
    return len(students)

    # Create a student
    create_student("john22", "John Paul", 22, ["Math", "Physics"], "Lagos", "100001")

    # Display student record
    print("Full Record:", display_student("john22"))

    # Display courses
    print("Courses:", display_courses("john22"))

    # Display zip code
    print("Zip Code:", display_zip("john22"))

    # Display city
    print("City:", display_city("john22"))

    # Add a new course
    print(add_course("john22", "Computer Science"))

    # Update a course
    update_course("john22", "Math", "Statistics")
    print("Updated Courses:", display_courses("john22"))

    # Update student details
    update_student("john22", age=25, city="Abuja")
    print("Updated Record:", display_student("john22"))

    # Total students
    print("Total Students:", total_students())
