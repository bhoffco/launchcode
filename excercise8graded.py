def course_grader(test_scores):
    # Your code here
    cutoff = 50
    for i in test_scores:
      if i < value:
        return false
      else:
        return true
    Print(i)

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()
