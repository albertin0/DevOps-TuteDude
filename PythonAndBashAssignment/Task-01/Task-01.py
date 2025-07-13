while True:
    score = input("Enter your score (or type 'exit' to quit): ")
    if score.lower() == 'exit':
        print("Exiting the program.")
        break
    try:
        score = float(score)
        if 0 <= score <= 100:
            if score >= 90:
                print("A")
            elif score >= 80:
                print("B")
            elif score >= 70:
                print("C")
            elif score >= 60:
                print("D")  
            else:
                print("F")
        else:
            print("Invalid score. Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric score.")