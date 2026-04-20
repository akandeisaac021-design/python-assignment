


students = {}


department_courses = {
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business"
}


def create_student(username, name, age, courses, city, zip_code):
    students[username] = {
        "name": name,
        "age": age,
        "courses": set(courses),
        "address": {"city": city, "zip": zip_code}
    }


def display_student(username):
    return students.get(username, "Student not found")


def display_courses(username):
    return students[username]["courses"]


def display_zip(username):
    return students[username]["address"]["zip"]


def display_city(username):
    return students[username]["address"]["city"]


def add_course(username, course):
    if course in department_courses and course not in students[username]["courses"]:
        students[username]["courses"].add(course)
        return f"{course} added successfully."
    return "Invalid or duplicate course."


def remove_course(username, course):
    students[username]["courses"].discard(course)

def update_course(username, old_course, new_course):
    if old_course in students[username]["courses"]:
        students[username]["courses"].remove(old_course)
        add_course(username, new_course)


def update_student(username, name=None, age=None, city=None, zip_code=None):
    if name: students[username]["name"] = name
    if age: students[username]["age"] = age
    if city: students[username]["address"]["city"] = city
    if zip_code: students[username]["address"]["zip"] = zip_code


def total_students():
    return len(students)


create_student("john22", "John Paul", 22, ["Math", "Physics"], "Lagos", "100001")


print("Full Record:", display_student("john22"))


print("Courses:", display_courses("john22"))

print("Zip Code:", display_zip("john22"))


print("City:", display_city("john22"))


print(add_course("john22", "Computer Science"))


update_course("john22", "Math", "Statistics")
print("Updated Courses:", display_courses("john22"))


update_student("john22", age=25, city="Abuja")
print("Updated Record:", display_student("john22"))


print("Total Students:", total_students())
