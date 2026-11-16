from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel,Field
import sqlite3
from fastapi.responses import RedirectResponse
class student(BaseModel):
    name:str
    age:int=Field(ge=18,le=30)
    gender: str
    marks:int
    image:str
    course:str
    status: int=Field(le=1,ge=0)

def get_connection():
    connection=sqlite3.connect(
        "students.db"
    )
    return connection
get_connection()
templates=Jinja2Templates(
    directory='templates'
)

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    q="""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        marks INTEGER,
        course TEXT,
        image TEXT,
        status INTEGER
    )
    """
    cursor.execute(q)
    connection.commit()
    connection.close()
create_table()
app=FastAPI()
@app.get('/')
def home(req:Request):
    Connection=get_connection()
    cursor=Connection.cursor()

    q="select * from students"
    cursor.execute(q)
    students1=cursor.fetchall()
    
    return templates.TemplateResponse(
        request=req,
        name='home.html',
        context={'stds':students1}

    )
@app.get('/student/add')
def add_student(req:Request):
    return templates.TemplateResponse(
        request=req,
        name='add-students.html',
        context={}

    )
@app.post('/student/add')
def create_std(name=Form(),age=Form(),gender=Form(),marks=Form(),course=Form(),image=Form(),status=Form()):
    students=student(name=name,
                      age=age,gender=gender,marks=marks,course=course,image=image,status=status)
    values=(students.name,students.age,students.gender,students.marks,students.course,students.image,students.status)
    connection=get_connection()
    cursor=connection.cursor()
    q="""
    INSERT INTO students(name ,age,gender,marks,course,image,status)
    values(?,?,?,?,?,?,?)
    """
    cursor.execute(q,values)
    connection.commit()
    connection.close()
    return RedirectResponse(url='/',status_code=303)
@app.get('/student/{std_id}')
def std_single(std_id:int,req:Request):
    Connection=get_connection()
    cursor=Connection.cursor()
    q='select * from students where id=?'
    cursor.execute(q,(std_id,))
    student=cursor.fetchone()
    Connection.close()
    return templates.TemplateResponse(
        request=req,
        name='single_std_details.html',
        context={
            'std':student
        }

    )
@app.get('/student/delete/{std_id}')
def delete_std(std_id:int,req:Request):
    Connection=get_connection()
    cursor=Connection.cursor()
    q = "DELETE FROM students WHERE id=?"
    cursor.execute(q, (std_id,))
    Connection.commit()
    Connection.close()
    return  RedirectResponse(url='/',status_code=303)

@app.get("/student/edit/{std_id}")
def edit_std(std_id: int, request: Request):

    Connection = get_connection()
    cursor = Connection.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (std_id,))
    std = cursor.fetchone()

    Connection.close()

    return templates.TemplateResponse(
    request=request,
    name="edit_student.html",
    context={"std": std}
)

@app.post("/student/edit/{std_id}")
def update_std(
    std_id: int,
    name: str = Form(...),
    age: int = Form(...),
    marks: int = Form(...),
    gender: str = Form(...),
    course: str = Form(...),
    image: str = Form(...),
    status: int = Form(...)
):

    Connection = get_connection()
    cursor = Connection.cursor()

    q = """
    UPDATE students
    SET name=?, age=?, gender=?, marks=?, course=?, image=?, status=?
    WHERE id=?
    """

    values = (name, age, gender, marks, course, image, status, std_id)

    cursor.execute(q, values)

    Connection.commit()
    Connection.close()

    return RedirectResponse(url="/", status_code=303)