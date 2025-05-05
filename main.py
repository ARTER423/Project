from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import engine, get_db
import models

# Создаем таблицы в базе данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Настройка статических файлов и шаблонов
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request, db: Session = Depends(get_db)):
    try:
        items = db.query(models.Item).all()
        return templates.TemplateResponse("index.html", {"request": request, "items": items})
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return templates.TemplateResponse("error.html", {"request": request})

@app.post("/add_item")
async def add_item(
    request: Request,
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    image_url: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        new_item = models.Item(
            name=name,
            description=description,
            price=price,
            image_url=image_url
        )
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        items = db.query(models.Item).all()
        return templates.TemplateResponse("index.html", {"request": request, "items": items})
    except Exception as e:
        print(f"Ошибка при добавлении элемента: {e}")
        db.rollback()
        return templates.TemplateResponse("error.html", {"request": request})