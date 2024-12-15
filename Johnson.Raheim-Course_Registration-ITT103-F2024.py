class Course:
    def __init__(self, course_id, course_name, course_fee):
        self.course_id = course_id  # Unique identifier for a course
        self.course_name = course_name  # name of the course
        self.course_fee = course_fee  # cost of the course


class Student:
    def __init__(self, student_id, student_name, student_email):
        self.student_id = student_id  # Unique identifier for a student
        self.student_name = student_name  # name of student
        self.student_email = student_email  # Contact Email of student
        self.courses = []  # List of courses the student is enrolled in
        self.fee_due = 0.0  # Total fee Amount for student
        self.payment_status = False  # Payment status (True if full payment is made or atleast 40%, False for pending/no payment made)

    def enroll(self, course):
        """Enroll the student in a course and update the balance."""
        # Registering selected student  in course selected
        if course in self.courses:  # checking if student is already in course
            print(
                f"{self.student_name} is already enrolled in {course.course_name}.")  # display if not added/ already in course
        else:
            self.courses.append(course)  # adding student to course 
            self.fee_due += course.course_fee  # add course cost to student balance
            print(f"{self.student_name} has been registered for {course.course_name}.")  # display if Added



class RegistrationSystem:
    def __init__(self):
        self.courses = []  # List to store course 
        self.students = []  # List to store student/s 

    def add_course(self):  # function for adding courses 
        """Add a new course."""
        try:
            course_id = int(input("Enter course ID: "))  # asking for Course Id number for course
        except ValueError: # checking if a Numeric value is enter
            print("Invalid input. Please enter a numeric value for the Course ID.")  #display if not 
            return
        course_name = input("Enter course name: ") # ask to enter the name of course
        try:
            course_fee = float(input("Enter course fee: ")) #asking for the fee for course
        except ValueError:#checking if a numeric value is used 
            print("Invalid input. Please enter a numeric value for the fee.")#display if not
            return
 
        if any(course.course_id == course_id for course in self.courses): # checking if course id already exist
            print("Course ID already exists.") #display if it is
            return
        if any(course.course_name == course_name for course in self.courses):#checking if course name already exist
            print("Course name already exists.") #display if it is
            return 
    # where course is  create and added
        new_course = Course(course_id, course_name, course_fee)
        self.courses.append(new_course)
        print(f"Course Name :'{course_name}',ID :'{course_id}' added successfully.") # Display when course is added

    def view_courses(self): # function to display all available courses 
        """Display all available courses."""
        if not self.courses: # checking if any course available 
            print("No courses available.") # display if not
        else:
            print("\nAvailable Courses:") # display all course
            for course in self.courses: 
                print(f"{course.course_name} (ID: {course.course_id}, Fee: ${course.course_fee:.2f})")

    def register_student_to_course(self):
        """Register a student for a course."""
        if not self.students:  # checking if any student is register  
            print("No students available. Please register a student first.")
            return
        if not self.courses:  # checking if any course was added
            print("No courses available. Please add a course first.")
            return
        # Selecting a student for course registration 
        print("\nSelect a student to register:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.student_name}")
        student_choice = input("Enter student ID: ")  # selecting student using id number
        # validating studentID/student exist
        student = next((s for s in self.students if str(s.student_id) == student_choice), None)
        if not student:
            print("Invalid student selection.")
            return
        # Selecting the course to be added for student
        print("\nSelect a course to register:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.course_name}")
        course_choice = input("Enter course ID: ")
        course = next((c for c in self.courses if str(c.course_id) == course_choice), None)
        # validating course exist
        if not course:  # in case course doesn't exist
            print("Invalid course selection.")
            return

        student.enroll(course)

    def register_student(self):
        """Register a new student."""
        if not self.courses: #checking if any student available
            print("No courses available for registration.") #display if not
            return

        name = input("Enter student name: ") # ask for student name to be entered
        email = input("Enter student email: ") # ask for student Email to be entered 
        try:
            student_id = int(input("Enter student ID number")) # asking for student id to be entered
        except ValueError: #checking if a numeric value is entered
            print("Invalid input. Please enter a numeric value for the Course ID.")
            return
        if any(student.student_id == student_id for student in self.students): # Checking if student di already exist
            print("Student ID already Exsit.") # display if it is
            return 
        if any(student.student_name == name for student in self.students): # checking if student name already exist
            print("Student name already Exsit.") #display if it is
            
   # where student is added/created
        student = Student(student_id, name, email)
        self.students.append(student)
        print(f"Student '{name}' registered successfully with ID: {student_id}.") # display when added

    def calculate_student_payment(self):
        """Calculate total payment for a student and allow payment based on entered amount."""
        if not self.students:
            print("No students available. Please register a student first.")
            return
        # Select a student to make payment for
        print("\nSelect a student to calculate payment:") 
        for student in self.students: # display all student
            print(f"ID: {student.student_id}, Name: {student.student_name}")# display all student
        student_choice = input("Enter student ID: ")  # ask to selected a student using id number

        # validate student ID Enter 
        student = next((s for s in self.students if str(s.student_id) == student_choice), None)
        if not student: # check if student exist
            print("Invalid student selection.") # display if is
            return
        if not student.courses: # check if student in courses 
            print(f"{student.student_name} is not enrolled in any courses.") #display if not
            return
        total_fee = sum(course.course_fee for course in student.courses) # calculate a student fee
        minimum_payment = total_fee * 0.4 # calculate minimum fee payment of 40%

        # Calculate total fee for Student
        total_fee = sum(course.course_fee for course in student.courses)
        print(f"\nTotal fee for {student.student_name}: ${total_fee:.2f}")
        print(f"Current outstanding fee: ${student.fee_due:.2f}")
        print(f"A minimum of 40% needs to be payed to be registed student:${minimum_payment}")

        # Ask student for payment
        try:
            amount_paid = float(input("Enter the amount being paid: "))
        except ValueError:  # make sure a Numeric value was entered
            print("Invalid input. Please enter a valid numeric value.")
            return

        #  payment Validation system
        if amount_paid >= total_fee:
            # Full payment validation Part 1
            student.payment_status = True
            student.fee_due = total_fee - amount_paid
            print(f"Full payment of ${amount_paid:.2f} completed. Student is now fully registered.")
        elif amount_paid >= minimum_payment:
            # Partial payment Validation Part 2  set at 40% of total
            student.fee_due = total_fee - amount_paid
            student.payment_status = True
            print(f"Payment of ${amount_paid:.2f} received. Remaining fee: ${student.fee_due:.2f}")
        else:
            # Payment invalidation part 3 insufficient amount less the 40%
            print(
                f"Payment of ${amount_paid:.2f} is insufficient. At least 40% of the total fee (${minimum_payment:.2f}) is required.")
            student.payment_status = False

    def view_students(self):
        """View all registered students."""
        if not self.students:
            print("No students registered.")
        else:
            print("\nRegistered Students:")
            for student in self.students:
                print(f"ID: {student.student_id}, Name: {student.student_name}, Email: {student.student_email}")
                print("-" * 40)

    def student_enrolled_in_course(self):
        if not self.students:  # checking if any student is register  
            print("No students available. Please register a student first.")
            return
        if not self.courses:  # checking if any course was added
            print("No courses available. Please add a course first.")
            return

        print("\nSelect a course to view student enrolled:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.course_name}")
            print("-" * 40)
        try:
            course_choice = int(input("Enter course ID: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for the Course ID.")
            return
        selected_course = next((c for c in self.courses if c.course_id == course_choice), None)
        if not selected_course:
            print("Course not found.")
            return

        enrolled_students = [student for student in self.students if selected_course in student.courses]
        if enrolled_students:
            print(f"\nStudents enrolled in {selected_course.course_name}:")
            for student in enrolled_students:
                print(f"ID: {student.student_id}, Name: {student.student_name}")
                print("-" * 40)
        else:
            print(f"No students are enrolled in {selected_course.course_name}.")

    def view_total_fee(self):
        """Display total fees and courses enrolled for each student."""
        if not self.students:
            print("No students registered.")
            return

        print("\nTotal Fees and Enrolled Courses:")
        for student in self.students:
            print(f"\nStudent ID: {student.student_id}, Name: {student.student_name}")
            if not student.courses:
                print("  No courses enrolled.")
            else:
                total_fee = sum(course.course_fee for course in student.courses)
                for course in student.courses:
                    print(f"  - {course.course_name} (Fee: ${course.course_fee:.2f})")
                print(f"  Total Fee Due: ${total_fee:.2f}")
                print(f"  Payment Status: {'Paid' if student.payment_status else 'Pending'}")
            print("-" * 40)
            
        

print("RLHS Admin Registration System")
username = input("Enter username :")
if username == "admin":
    registration_system = RegistrationSystem()

    while True:
        print(
            "\n1. Add Course\n2. View Courses\n3. Register Student\n4. View Students\n5. Register Student to Course\n6. Calculate Student Payment\n7. View fee for enrolled courses\n8. View student in a course\n9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            registration_system.add_course()
        elif choice == "2":
            registration_system.view_courses()
        elif choice == "3":
            registration_system.register_student()
        elif choice == "4":
            registration_system.view_students()
        elif choice == "5":
            registration_system.register_student_to_course()
        elif choice == "6":
            registration_system.calculate_student_payment()
        elif choice == "7":
            registration_system.view_total_fee()
        elif choice == "8":
            registration_system.student_enrolled_in_course()
        elif choice == "9":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
