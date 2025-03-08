import os
import mysql.connector
from mysql.connector import Error

# Get the database details from the environment
db_host = os.environ.get('DB_HOST', 'localhost')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER_NAME')
db_pass = os.environ.get('DB_USER_PASSWORD')


# Set the list of Placement Eligibilty Ctiteria queries

Eligibility1 = """SELECT s.student_id,s.name,s.course_batch,
                   p.language,p.problems_solved
                   FROM students s,programming p
                   WHERE s.student_id = p.student_id 
                   AND p.problems_solved >= %s;
              """

Eligibility2 = """SELECT s.student_id,s.name,s.course_batch,
                   p.language,p.latest_project_score
                   FROM students s, programming p
                   WHERE s.student_id = p.student_id
                   AND p.latest_project_score >= %s;
              """

Eligibility3 = """SELECT s.student_id, s.name, s.course_batch, p.language,
                   p.mini_projects FROM students s,programming p
                   where s.student_id = p.student_id
                   AND p.mini_projects >= %s;
              """

Eligibility4 = """SELECT s.student_id,s.name,s.course_batch,
                   ROUND(((ss.communication+ ss.teamwork
                   + ss.presentation+ss.leadership
                   + ss.critical_thinking
                   + ss.interpersonal_skills)/600)*100) as soft_skill_score 
                   FROM students s,soft_skills ss 
                   WHERE s.student_id =ss.student_id
                   AND ROUND(((ss.communication+ ss.teamwork
                   + ss.presentation+ss.leadership
                   + ss.critical_thinking
                   + ss.interpersonal_skills)/600)*100) >= %s;
              """


def runQuery(query,queryParam):
    """Get database values from the environment 
       and execute the respective Placement Eligibility criteria query
       passed with the query parameter
    """

    try:
        # Get the database connection from the environment
        connection = mysql.connector.connect(host=db_host, database = db_name,
                                             user=db_user, password=db_pass)
        cursor = connection.cursor()

        # Execute the query  
        cursor.execute(query,queryParam)

        # Get the data for the query executed 
        queryData = cursor.fetchall()
        # Set the column names
        col_names = [desc[0] for desc in cursor.description]
            
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

        return queryData,col_names
