import pandas as pd
from faker import Faker
import InsertFakeData as ifd

fake = Faker()

# Set possible values for fake data
genders = ['Male', 'Female', 'Other']
course_prefix = ['AIML', 'DS', 'DE', 'FSD', 'DA']
languages = ['Python','SQL','JAVA','C++','C','Javascript','.Net']
placement_status_values = ['Ready', 'Not Ready','Placed']


def Create_Insert_Fake_Data(nof_students, nof_Programs):
    """Calls respective create table data functions 
       and calls the insert data function with the respective table data
       and executes the respective insert table query passed as parameter.
       
       As per the table relationship
       For every Student record, passed number of Progrmaming
       records is created
       For every Student record, one Soft_Skills and Placements
       record is created
    """

    # Create Students table data
    students_df = create_students_data(nof_students)
    # Insert into Students table data
    ifd.insertData(ifd.insert_students_query, students_df)

    # Create Programming table data
    program_data_df = create_programming_data(nof_students, nof_Programs)
    # Insert into Programming table data
    ifd.insertData(ifd.insert_programming_data_query,program_data_df)
    
    # Create Soft_Skills table data
    soft_skills_data_df = create_soft_skills_data(nof_students)
    # Insert into Soft_Skills table data
    ifd.insertData(ifd.insert_soft_skills_data_query,soft_skills_data_df)
    
    # Create Placements table data
    placements_data_df = create_placements_data(nof_students)
    # Insert into Placements table data
    ifd.insertData(ifd.insert_placements_data_query,placements_data_df)


def create_students_data(nof_students):
    """Creates nof students records specified with Faker data
       and returns the data in a dataframe
    """
    students = []

    for i in range(nof_students):
        
        student_id = i+1
        gender = fake.random_element(genders)

        # Set faker name based on gender
        if gender == "Male" :
            name = fake.name_male() 
        elif gender == "Female" :
            name = fake.name_female() 
        else:
            name = fake.name()

        age = fake.random_int(18,60)
        email = fake.email()
        phone = fake.phone_number()
        enrollment_year = fake.random_int(2020,2025)
        course_batch = fake.random_element(course_prefix) + "B" + str(fake.random_int(0,5))
        city = fake.city()
        graduation_year = fake.random_int(enrollment_year,2026)

        students.append({'student_id':student_id,
                         'name': name,
                         'age': age,
                         'gender': gender,
                         'email': email,
                         'phone': phone,
                         'enrollment_year': enrollment_year,
                         'course_batch': course_batch,
                         'city': city,
                         'graduation_year': graduation_year
                        })
          
    return pd.DataFrame(students)


def create_programming_data(nof_students, nof_Programs):
    """Creates nof Program records per nof students' records
       specified with Faker data
       and returns the data in a dataframe
    """

    program_data = []
    pcount = 0

    for i in range(nof_students):

        for j in range(nof_Programs):
            
            pcount+= 1
            programming_id  = pcount
            student_id = i+1
            language = fake.random_element(languages)
            problems_solved = fake.random_int(10,300)
            assessments_completed = fake.random_int(0,20)
            mini_projects = fake.random_int(0,5)
            certifications_earned = fake.random_int(0,10)
            latest_project_score = fake.random_int(0,100)
            
            program_data.append({'programming_id': programming_id,
                                 'student_id': student_id,
                                 'language': language,
                                 'problems_solved': problems_solved, 
                                 'assessments_completed': assessments_completed,
                                 'mini_projects': mini_projects,
                                 'certifications_earned': certifications_earned,
                                 'latest_project_score': latest_project_score,
                                })
            
    pcount = j+1
    return pd.DataFrame(program_data)


def create_soft_skills_data(nof_students):
    """Creates one soft_skill record per nof students' records specified 
       with Faker data and returns the data in a dataframe
    """

    soft_skills_data = []

    for i in range(nof_students):

        soft_skill_id = i+1
        student_id = i+1
        communication = int(fake.random_int(0,100))
        teamwork = fake.random_int(0,100)
        presentation = fake.random_int(0,100)
        leadership = fake.random_int(0,100)
        critical_thinking = fake.random_int(0,100)
        interpersonal_skills = fake.random_int(0,100)
        
        soft_skills_data.append({'soft_skill_id': soft_skill_id,
                                 'student_id': student_id,
                                 'communication': communication,
                                 'teamwork': teamwork, 
                                 'presentation': presentation,
                                 'leadership': leadership,
                                 'critical_thinking': critical_thinking,
                                 'interpersonal_skills': interpersonal_skills
                                })

    return pd.DataFrame(soft_skills_data)


def create_placements_data(nof_students):
    """Creates one Placement record per nof students' records specified
       with Faker data and returns the data in a dataframe
    """

    placements_data = []

    for i in range(nof_students):

        placement_id = i+1
        student_id = i+1
        mock_interview_score = fake.random_int(0,100)
        internships_completed = fake.random_int(0,10)
        placement_status = fake.random_element(placement_status_values)
        company_name = fake.company()
        placement_package = fake.random_int(30000, 100000)
        interview_rounds_cleared = fake.random_int(0,5)
        placement_date = fake.date_this_year()
        
        placements_data.append({'placement_id': placement_id,
                                 'student_id': student_id,
                                 'mock_interview_score': mock_interview_score,
                                 'internships_completed': internships_completed, 
                                 'placement_status': placement_status,
                                 'company_name': company_name,
                                 'placement_package': placement_package,
                                 'interview_rounds_cleared': interview_rounds_cleared,
                                 'placement_date': placement_date
                                })

    return pd.DataFrame(placements_data)
