import os
import mysql.connector
from mysql.connector import Error


db_host = os.environ.get('DB_HOST', 'localhost')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER_NAME')
db_pass = os.environ.get('DB_USER_PASSWORD')

# Set the list of Data Insight queries

insight1 = """SELECT s.course_batch,
                ROUND(AVG((p.problems_solved + p.assessments_completed
                + p.mini_projects + p.certifications_earned
                + p.latest_project_score)/5)) as AvgProgrammingPerformance
                FROM students s, programming p 
                WHERE s.student_id = p.student_id 
                GROUP BY s.course_batch;
           """

insight2 = """SELECT s.student_id,s.name,s.course_batch,p.placement_status 
                FROM students s,placements p
                WHERE s.student_id = p.student_id and p.placement_status = 'Ready';
           """

insight3 = """SELECT communication,teamwork,presentation,leadership,
                critical_thinking,interpersonal_skills
                FROM soft_skills;
           """

insight4 = """SELECT students.name,students.course_batch,
                placements.placement_status, placements.company_name,
                placements.placement_package,placements.placement_date 
                FROM students
                INNER JOIN placements ON students.student_id = placements.student_id 
                WHERE placements.placement_status = 'Placed' 
                ORDER BY students.course_batch;
          """

insight5 = """SELECT s.student_id,s.name,s.course_batch,
                round(((ss.communication+ ss.teamwork+ ss.presentation
                + ss.leadership+ss.critical_thinking
                + ss.interpersonal_skills)/600)*100) as soft_skill_score
                FROM students s,soft_skills ss
                WHERE s.student_id =ss.student_id
                AND ROUND(((ss.communication+ ss.teamwork
                + ss.presentation+ss.leadership+ss.critical_thinking
                + ss.interpersonal_skills)/600)*100) >= 75;"""

insight6 = """SELECT s.student_id,s.name,s.course_batch,s.graduation_year
                FROM students s 
                ORDER BY graduation_year,course_batch;
           """

insight7 = """SELECT s.course_batch as Course,
                COUNT(s.course_batch) as NofStudents
                FROM students s
                GROUP BY course_batch order by NofStudents desc limit 3;
           """

insight8 = """SELECT language as ProgrammingLanguage,
                COUNT(student_id) as NofStudents
                FROM programming
                GROUP BY language;
           """

insight9 = """SELECT s.student_id,s.name,s.course_batch,p.placement_status,
                p.interview_rounds_cleared as InterviewRoundsCleared
                FROM students s
                INNER JOIN placements p on s.student_id = p.student_id 
                WHERE p.placement_status = 'Ready'
                AND p.interview_rounds_cleared >=
                (SELECT MAX(interview_rounds_cleared) FROM placements);
           """

insight10 = """SELECT s.student_id,s.name,s.course_batch,
                 ss.communication as communication_skill_score 
                 FROM students s,soft_skills ss
                 WHERE s.student_id =ss.student_id 
                 AND ss.communication >90 limit 10;
            """


def runQuery(query):
    """Get database values from the environment 
       and execute the respective Insights query passed
    """

    try:
        # Get the database connection from the environment
        connection = mysql.connector.connect(host=db_host, database = db_name,
                                              user=db_user, password=db_pass)
        cursor = connection.cursor()

        # Execute the query   
        cursor.execute(query)

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