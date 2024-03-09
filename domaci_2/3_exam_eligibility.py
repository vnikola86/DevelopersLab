def check_exam_eligibility(attendance_percentage, all_seminar_works_submitted):

    if attendance_percentage > 75 and all_seminar_works_submitted == 1:
        return "The student is eligible to take the exam."
    else:
        return "The student is not eligible to take the exam."

attendance_percentage = 80
seminar_works_status = 1

eligibility_message = check_exam_eligibility(attendance_percentage, seminar_works_status)
print(eligibility_message)
