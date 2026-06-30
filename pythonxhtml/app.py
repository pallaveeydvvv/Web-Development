import sys 
import csv
import matplotlib.pyplot as plt
#print(sys.argv)
if len(sys.argv) < 3:
    print("Please provide the required arguments.")
elif sys.argv[1].strip() == "-s":
    
    student_id = sys.argv[2]

    student_data=[]

    with open("data.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row
        for row in reader:
            if row[0].strip() == student_id:
                student_data.append(row)
    

    if len(student_data) == 0:
        with open("output.html", 'w') as file:
            file.write("<!DOCTYPE html>\n")
            file.write("<html>\n")
            file.write("<head>\n")
            file.write("<title>Something Went Wrong</title>\n")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write("<h1>Wrong Inputs</h1>\n")
            file.write("<p>Something went wrong</p>\n")
            file.write("</body>\n")
            file.write("</html>\n")
            
    else:
        total_marks = 0
        for course in student_data:
            total_marks += int(course[2])
    
        
        with open("output.html", 'w') as file:
        
            file.write("<!DOCTYPE html>\n")
            file.write("<html>\n")  

            file.write("<head>\n")
            file.write("<title>Student Details</title>\n")
            file.write("</head>\n")
                    
            file.write("<body>\n")
            file.write("<h1>Student Details</h1>\n")
            file.write("<table border='1'>\n")
            file.write("<tr>\n")
            file.write("<th>Student ID</th>")
            file.write("<th>Course ID</th>")
            file.write("<th>Marks</th>")
            file.write("</tr>\n")
            for course in student_data:
                file.write("<tr>\n")
                file.write(f"<td>{course[0]}</td>\n")
                file.write(f"<td>{course[1]}</td>\n")
                file.write(f"<td>{course[2]}</td>\n")
                file.write("</tr>\n")
            file.write("<tr>\n")
            file.write(f"<td colspan='2'>Total Marks</td>\n")
            file.write(f"<td>{total_marks}</td>\n")
            file.write("</tr>\n")
            file.write("</table>\n")
            file.write("<p>This page is generated using Python.</p>\n")
            file.write("</body>\n")

            file.write("</html>\n")

elif sys.argv[1].strip() == "-c":
    course_id = sys.argv[2]
    course_data = []
    
    with open("data.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row
        for row in reader:
            if row[1].strip() == course_id:
                course_data.append(row)

    if len(course_data) == 0:
        with open("output.html", 'w') as file:
            file.write("<!DOCTYPE html>\n")
            file.write("<html>\n")
            file.write("<head>\n")
            file.write("<title>Something Went Wrong</title>\n")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write("<h1>Wrong Inputs</h1>\n")
            file.write("<p>Something went wrong</p>\n")
            file.write("</body>\n")
            file.write("</html>\n")
    else:         
        total_marks = 0
        maximum_marks = 0
        marks=[]
        for course in course_data:
            total_marks += int(course[2])
            if int(course[2]) > maximum_marks:
                maximum_marks = int(course[2])
            marks.append(int(course[2]))
        average_marks = total_marks/len(course_data)
        plt.figure()
        plt.hist(marks)
        plt.title("Marks Distribution")
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.savefig("figure_1.png")
        plt.close()
        
        with open("output.html", 'w') as file:

            file.write("<!DOCTYPE html>\n")
            file.write("<html>\n")

            file.write("<head>\n")
            file.write("<title>Course Data</title>\n")
            file.write("</head>\n")
                    
            file.write("<body>\n")
            file.write("<h1>Course Details</h1>\n")
            file.write("<table border='2'>\n")
            file.write("<tr>\n")
            file.write("<th>Average Marks</th>")
            file.write("<th>Maximum Marks</th>")
            file.write("</tr>\n")
            file.write("<tr>\n")
            file.write(f"<td>{average_marks}</td>\n")
            file.write(f"<td>{maximum_marks}</td>\n")
            file.write("</tr>\n")
            file.write("</table>\n")
            file.write("<img src='figure_1.png' alt='Histogram of Marks'>\n")
            file.write("<p>This page is generated using Python.</p>\n")
            file.write("</body>\n")
            file.write("</html>\n")

    
   