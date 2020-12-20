# *E-Laaj*
## Rural Healthcare Management System

Making healthcare in rural areas more accessible.

# *Tech-Stack*
- Frontend
  - HTML
  - CSS
- Backend
  - Flask
- Database
 - SQLite
 
![Screenshot (814)](https://user-images.githubusercontent.com/61280281/102720683-c13b5080-431b-11eb-9fc8-25fc764e0ed8.png)
 
![Screenshot (815)](https://user-images.githubusercontent.com/61280281/102720682-bf718d00-431b-11eb-9229-d73d53f83e07.png)


# Dataflow

```
Homepage --> Different Languages Implemented
|
|
Patient (Phone Number Login) - Phone Number is in the database - PATIENT PORTAL
|                                   |
|                                   |
|                                   SIGNUP PAGE
|
|
DOCTOR (Proper Login Page)
  - Name
  - Age
  - Speciality
  - Phone Number
  - License ID
  - Years of Experience
  - Location (Address)


Patient Portal
- Make an appointment 
  - Current problems that the patient is facing.
- Uploading Reports
- Patient History (Ask a bunch of Questions)
  - Blood Group
  - Diabetic History
  - etc.
  
Doctor's Portal
- Upcoming appointments 
  - Accept/Reject
- History of Patients

```

## *Setup*

1. Download Python 3,
2. CD into the project directory.
3. Run 
`python3 -m pip install venv`

4. Now run 
`python3 -m venv env`

5. Now wait until it is done and if you are on windows type 
`env/Scripts/activate`

6. Now run 
`python3 -m pip install -r requirements.txt`

7. Then type 
`set FLASK_APP="elaaj"`

8. Then 
`set FLASK_ENV="development"`

9. Then 
`flask run`


