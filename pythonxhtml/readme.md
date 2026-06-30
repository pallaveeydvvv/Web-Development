# 📊 Student & Course Data Analyzer

A Python-based application that processes student records from a CSV file and automatically generates an HTML report. Depending on the user's input, the program can either display detailed information for a specific student or provide statistical analysis for a particular course, including a histogram of marks.

This project demonstrates the use of **Python**, **CSV file handling**, **command-line arguments**, **HTML generation**, and **data visualization using Matplotlib**.

---

## 🚀 Features

### 👨‍🎓 Student Mode (`-s`)

* Search records using a Student ID.
* Display all enrolled courses and corresponding marks.
* Calculate and display the total marks obtained.
* Generate a clean HTML report (`output.html`).

### 📚 Course Mode (`-c`)

* Search records using a Course ID.
* Calculate:

  * Average Marks
  * Maximum Marks
* Generate a histogram showing the distribution of marks.
* Save the histogram as `figure_1.png`.
* Generate an HTML report containing both statistics and the histogram.

### ❌ Error Handling

If an invalid Student ID or Course ID is entered, the program automatically generates an HTML page displaying an appropriate error message.

---

## 🛠️ Technologies Used

* Python 3
* CSV Module
* Matplotlib
* HTML

---

## 📂 Project Structure

```
Student-Course-Analyzer/
│
├── app.py               # Main Python program
├── data.csv             # Input dataset
├── output.html          # Generated HTML report
├── figure_1.png         # Histogram (generated in Course Mode)
└── README.md
```

---

## 📋 Dataset Format

The input CSV file should follow this structure:

| Student ID | Course ID | Marks |
| ---------- | --------- | ----- |
| 1001       | CS101     | 85    |
| 1001       | MA102     | 91    |
| 1002       | CS101     | 78    |

---

## ▶️ How to Run

### Generate Student Report

```bash
python app.py -s <Student_ID>
```

Example:

```bash
python app.py -s 1001
```

This generates:

* `output.html`

containing the student's course details and total marks.

---

### Generate Course Report

```bash
python app.py -c <Course_ID>
```

Example:

```bash
python app.py -c CS101
```

This generates:

* `output.html`
* `figure_1.png`

showing course statistics and the marks distribution.

---

## 📊 Output

### Student Report

* Student ID
* Course IDs
* Marks obtained
* Total Marks

### Course Report

* Average Marks
* Maximum Marks
* Histogram of Marks Distribution

---

## 📈 Learning Outcomes

This project helped in understanding:

* Reading and processing CSV files
* Working with command-line arguments (`sys.argv`)
* Data filtering and aggregation
* Dynamic HTML generation using Python
* Data visualization with Matplotlib
* Basic file handling and report generation

---

## 👨‍💻 Author

**Pallavee**

This project was developed as part of my learning journey in Python and Data Visualization. It strengthened my understanding of file handling, report generation, and graphical representation of data while working with real-world datasets.

---

⭐ If you found this project useful, consider giving the repository a star!
