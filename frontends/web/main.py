import uuid

from fastapi import FastAPI, Cookie
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from application.engine.engine import Engine
from application.managers.manager import GameObjectManager, LineManager, MovementManager
from core.models.config import DataConfig
from infrastructure.factories.factory import CircleFactory, DefaultLineFactory
from infrastructure.lines.line import BrightnessComparisonStrategy, DefaultBrightnessCalculator

app = FastAPI()
templates = Jinja2Templates(directory="templates")

screen_size = (800, 800)
config = DataConfig(
    count_obj=15,
    circle_radius=15,
    start_speed=1.05,
    width_of_line=10,
    upper_limit=50,
    lower_limit=200
)

engines = {}

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request, client_id: str = Cookie(default=None)):
    if client_id is None:
        return RedirectResponse(url="/get_client_id")
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/get_client_id")
async def get_client_id():
    client_id = str(uuid.uuid4())
    response = RedirectResponse(url='/')
    response.set_cookie(key="client_id", value=client_id, httponly=True)
    return response


@app.get("/state")
async def get_state(client_id: str = Cookie(default=None)):
    global engines
    if client_id is None:
        return JSONResponse(status_code=400, content={"detail": "No client_id"})

    if client_id not in engines.keys():
        obj_manager = GameObjectManager(screen_size, config.circle_radius, config.start_speed,
                                        CircleFactory())
        line_manager = LineManager(config.upper_limit, config.lower_limit, config.width_of_line,
                                   DefaultLineFactory(DefaultBrightnessCalculator(), BrightnessComparisonStrategy()))
        movement_manager = MovementManager(screen_size)
        engines[client_id] = Engine(screen_size, config.count_obj, obj_manager, line_manager, movement_manager)

    engine = engines[client_id]
    circles = [{"pos": circle.pos, "radius": circle.radius} for circle in engine.circles]
    lines = [{"start_pos": line.get_start_pos(), "end_pos": line.get_end_pos(), "width": line.width,
              "brightness": line.brightness} for line in engine.lines]

    engine.move_figures()
    return {"circles": circles, "lines": lines}


@app.get("/get_initial_data")
async def start_color():
    return {"color": [255, 200, 0]}
