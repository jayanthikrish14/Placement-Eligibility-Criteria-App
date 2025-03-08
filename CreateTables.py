import os
import mysql.connector
from mysql.connector import Error

# Get the database details from the environment
db_host = os.environ.get('DB_HOST', 'localhost')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER_NAME')
db_pass = os.environ.get('DB_USER_PASSWORD')

# Set the create table queries
create_Students_tbl_query = """create table if not exists Students( 
                                student_id int not null primary key,
                                name Varchar(100) not null,
                                age int not null,
                                gender varchar(10) not null,
                                email varchar(100) not null,
                                phone varchar(100) not null,
                                enrollment_year year not null ,
                                course_batch varchar(100) not null,
                                city varchar(100) not null,
                                graduation_year year not null
                                );"""

create_Programming_tbl_query = """create table if not exists Programming(
                                programming_id int not null primary key,
                                student_id int not null,
                                language Varchar(100) not null,
                                problems_solved int not null,
                                assessments_completed int not null,
                                mini_projects int not null,
                                certifications_earned int not null,
                                latest_project_score int not null,
                                foreign key(student_id) references Students(student_id)
                                );"""

create_Soft_Skills_tbl_query = """create table if not exists Soft_Skills(
                                soft_skill_id int not null primary key,
                                student_id int not null,
                                communication int not null,
                                teamwork int not null,
                                presentation int not null,
                                leadership int not null,
                                critical_thinking int not null,
                                interpersonal_skills int not null,
                                foreign key(student_id) references Students(student_id)
                                );"""                              

create_Placements_tbl_query = """create table if not exists Placements(
                                placement_id int not null primary key,
                                student_id int not null,
                                mock_interview_score int not null,
                                internships_completed int not null,
                                placement_status Varchar(100) not null,
                                company_name Varchar(100) not null,
                                placement_package int not null,
                                interview_rounds_cleared int not null,
                                placement_date date not null,
                                foreign key(student_id) references Students(student_id)
                                );"""  

def createTable(query):
    """Get database values from the environment 
       and execute the insert table query passed as parameter
    """
        
    try:
        # Get the database connection from the environment
        connection = mysql.connector.connect(host=db_host, database = db_name,
                                                user=db_user, password=db_pass)
        
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(query)

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
