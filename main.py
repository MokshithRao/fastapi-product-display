from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(req:Request):
    sai_hi = "Hello, Welcome to my cafe"
    return templates.TemplateResponse(
        request=req,
        name="home.html"
    )


@app.get('/products', response_class=HTMLResponse)
def products(req:Request):
    products = [(1, "laptop", 70000), (2, "iphone", 87000)]
        
    return  templates.TemplateResponse(
        request=req,
        name="products.html",
        context={"products": products}
    )