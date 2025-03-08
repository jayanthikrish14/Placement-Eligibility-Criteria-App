import os
import mysql.connector
from mysql.connector import Error

# Get the database details from the environment
db_host = os.environ.get('DB_HOST', 'localhost')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER_NAME')
db_pass = os.environ.get('DB_USER_PASSWORD')

# Set the insert table queries
insert_students_query = """insert into Students(student_id,name,age,gender,
                            email,phone,enrollment_year,course_batch,city,
                            graduation_year) 
                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                        """
    
insert_programming_data_query = """insert into Programming(programming_id,
                                    student_id,language,problems_solved,
                                    assessments_completed,mini_projects,
                                    certifications_earned,latest_project_score) 
                                    values(%s,%s,%s,%s,%s,%s,%s,%s);
                                """
    
insert_soft_skills_data_query = """insert into Soft_Skills(soft_skill_id,
                                    student_id,communication,teamwork,
                                    presentation,leadership,
                                    critical_thinking,interpersonal_skills) 
                                    values(%s,%s,%s,%s,%s,%s,%s,%s);
                                """
    
insert_placements_data_query = """insert into Placements(placement_id,
                                    student_id,mock_interview_score,
                                    internships_completed,placement_status,
                                    company_name,placement_package,
                                    interview_rounds_cleared,placement_date) 
                                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s);
                                """


def insertData(query, df):
    """Get database values from the environment 
       and execute the insert table query and data passed as parameters
    """
      
    try:
        # Get the database connection from the environment
        connection = mysql.connector.connect(host=db_host, database = db_name,
                                              user=db_user, password=db_pass)

        cursor = connection.cursor()

        data = [list(x) for x in df.values ]

        # convert the int64 to int for soft_skills table data
        if query == insert_soft_skills_data_query:
            newData = []
            for val in data:
                val = list(map(int, val))
                newData.append(val)
            data = newData
                 
        cursor.fast_executemany = True
        # Execute the query
        cursor.executemany(query,data)
            
    except Error as e :
        print ("error", e)
        pass
    
    except Exception as e:
        print ("Unknown error %s", e)
    
    finally:
        #closing database connection.
        if(connection and connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()    
