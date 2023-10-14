from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from general_pages.route_homepage import general_pages_router
from database.db_session import engine  # new
from database.base_class import Base  # new

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


def include_router(app):
	app.include_router(general_pages_router)


def configure_static(app):
	app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():  # new
	Base.metadata.create_all(bind=engine)


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()  # new
	return app


app = start_application()
