from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from animation.action.engine import Engine, EngineConfig

app = FastAPI()
templates = Jinja2Templates(directory="templates")

screen_size = (800, 800)
config = EngineConfig(
    count_obj = 23,
    circle_radius = 15,
    start_speed= 1.05,
    width_of_line = 10,
    upper_limit = 50,
    lower_limit = 200
)
engine = Engine(screen_size, config)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/state")
async def get_state():
    global engine

    circles = [{"pos": circle.pos, "radius": circle.radius} for circle in engine.circles]
    lines = [{"start_pos": line.start_pos, "end_pos": line.end_pos, "width": line.width, "brightness": line.brightness} for line in engine.lines]

    engine.move_figures()

    return JSONResponse(content={"circles": circles, "lines": lines})

@app.get("/get_initial_data")
async def start_color():
    return {"color": [255, 200, 0]}
