import matplotlib
import matplotlib.pyplot as plt
import numpy as np

computer_support_technician = []
digital_marketer = []
frontend_developer = []
security_specialist = []
ml_engineer = []
marketing_analyst = []
hr_analyst = []
software_engineer = []
data_scientist = []

job_list = [computer_support_technician, digital_marketer, frontend_developer, security_specialist, ml_engineer, marketing_analyst, hr_analyst, software_engineer, data_scientist]
job_list_str = ['Computer Support Technician', 'Digital Marketer', 'Front-End Developer', 'Security Specialist', 'ML Engineer', 'Marketing Analyst', 'HR Analyst', 'Software Engineer', 'Data Scientist']


date = ['30', '1', '2', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']

data = open("JobPostingsData", "r").readlines()

for i in range(len(data)):
    data[i] = data[i].split()
    data[i][0] = data[i][0].split("-")

for j in range(0, len(data)):
    if j % 9 == 0:
        computer_support_technician.append(int(data[j][-1]))
    elif j % 9 == 1:
        digital_marketer.append(int(data[j][-1]))
    elif j % 9 == 2:
        frontend_developer.append(int(data[j][-1]))
    elif j % 9 == 3:
        security_specialist.append(int(data[j][-1]))
    elif j % 9 == 4:
        ml_engineer.append(int(data[j][-1]))
    elif j % 9 == 5:
        marketing_analyst.append(int(data[j][-1]))
    elif j % 9 == 6:
        hr_analyst.append(int(data[j][-1]))
    elif j % 9 == 7:
        software_engineer.append(int(data[j][-1]))
    else:
        data_scientist.append(int(data[j][-1]))

for job in range(len(job_list)):
    plt.figure(figsize=(15, 10))
    plt.plot(date, job_list[job])
    plt.xlabel('Date')
    plt.ylabel('Postings')
    plt.title('June 30 - July 27 \"' + job_list_str[job] + "\" Job Postings")

    plt.savefig('June 30 - July 27 ' + job_list_str[job] + " Job Postings")
    plt.show()