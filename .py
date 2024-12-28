def get_rubric():
    # Get rubric details from the user
    rubric = {}
    print("Please enter the rubric criteria and their maximum points")
    while True:
        criterion = input("Enter a rubric criterion or type 'done' to finish: ")
        if criterion.lower() == 'done':
            break
        try:
            criterion_name, max_points = criterion.split(":")
            rubric[criterion_name.strip()] = float(max_points.strip())
        except ValueError:
            print("Invalid input format. Please enter as 'Criterion: MaxPoints'.")
    return rubric

def get_student_work(rubric):
    # Get the student's performance for each rubric criterion
    student_scores = {}
    print("\nNow, please enter the student's performance for each criterion (0 to max points):")
    for criterion, max_points in rubric.items():
        while True:
            try:
                score = float(input(f"Score for {criterion} (Max {max_points}): "))
                if 0 <= score <= max_points:
                    student_scores[criterion] = score
                    break
                else:
                    print(f"Please enter a score between 0 and {max_points}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return student_scores

def calculate_final_grade(rubric, student_scores):
    # Calculate the final grade based on rubric
    total_max_points = sum(rubric.values())
    total_score = sum(student_scores.values())
    grade_percentage = (total_score / total_max_points) * 100
   
    if grade_percentage >= 90:
        grade = "A"
    elif grade_percentage >= 80:
        grade = "B"
    elif grade_percentage >= 70:
        grade = "C"
    elif grade_percentage >= 60:
        grade = "D"
    else:
        grade = "F"
   
    return grade_percentage, grade

def main():
    print("Welcome to the Grading Robot!")
   
    # Step 1: Get the rubric
    rubric = get_rubric()
   
    # Step 2: Get the student's work
    student_scores = get_student_work(rubric)
   
    # Step 3: Calculate the final grade
    grade_percentage, grade = calculate_final_grade(rubric, student_scores)
   
    # Step 4: Show results
    print("\n--- Grading Summary ---")
    for criterion, score in student_scores.items():
        print(f"{criterion}: {score}/{rubric[criterion]}")
   
    print(f"\nTotal Score: {grade_percentage:.2f}%")
    print(f"The student's final grade is: {grade}")

if __name__ == "__main__":
    main()
