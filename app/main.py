import pathlib
from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app import db
from cassandra.cqlengine.management import sync_table
from app.user.models import User
from app.user.schemas import UserLoginSchema, UserSignupSchema

# pathlib giving /app path saving in base
# .parent give app/
BASE_DIR = pathlib.Path(__file__).resolve().parent
# giving path as /app/templates
TEMPLATE_DIR = BASE_DIR / "templates"
# passing these path to jinja engine in variable templates
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))
app = FastAPI()


@app.on_event("startup")
def on_startup():
    db.get_session()
    sync_table(User)


@ app.get("/", response_class=HTMLResponse)
def root(request: Request):
    context = {
        "request": request,
        "name": "Mubbaseer"
    }
    # jinjaTemplates: request argument require
    return templates.TemplateResponse("home.html", context)


@ app.get("/login", response_class=HTMLResponse)
def login_get_view(request: Request):
    # jinjaTemplates: request argument require
    return templates.TemplateResponse("auth/login.html", {
        "request": request,
    })


@ app.post("/login", response_class=HTMLResponse)
def login_get_view(request: Request, email: str = Form(...), password: str = Form(...)):
    print(email, password)
    # jinjaTemplates: request argument require
    return templates.TemplateResponse("auth/login.html", {
        "request": request
    })


@ app.get("/signup", response_class=HTMLResponse)
def signup_get_view(request: Request):
    # jinjaTemplates: request argument require
    return templates.TemplateResponse("auth/signup.html", {
        "request": request,
    })


@ app.post("/signup", response_class=HTMLResponse)
def signup_get_view(request: Request,
                    email: str = Form(...),
                    password: str = Form(...),
                    password_confirm=Form(...)
                    ):
    print(email, password, password_confirm)
    # jinjaTemplates: request argument require
    return templates.TemplateResponse("auth/signup.html", {
        "request": request
    })


@app.get("/users")
def users_list():
    q = User.objects.all()
    return list(q)


@app.post("/create_user")
def create_user(user):
    db.get_session()
    sync_table(User)
    return "Done"
