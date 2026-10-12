from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db_connection


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="home.html"
    )


@app.get('/products', response_class=HTMLResponse)
def products(req: Request):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    connection.close()


    return  templates.TemplateResponse(
        request=req,
        name="products.html",
        context={"products": products}
    )