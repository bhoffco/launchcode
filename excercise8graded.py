def course_grader(test_scores):
    # Your code here
    score_total = sum(test_scores)
    avg = score_total / len(test_scores)

    for i in test_scores:
        if i < 50:
            return "fail"
        elif avg < 70:
            return "fail"
    return "pass"


def main():
    print(course_grader([100, 75, 45]))     # "fail"
    print(course_grader([100, 70, 85]))     # "pass"
    print(course_grader([80, 60, 60]))      # "fail"
    print(course_grader([80, 80, 90, 30, 80]))  # "fail"
    print(course_grader([70, 70, 70, 70, 70]))  # "pass"


if __name__ == "__main__":
    main()
