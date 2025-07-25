"""main filе"""

from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from fastapi_application.core.config import settings


from fastapi_application.api import router as api_router
from fastapi_application.core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI): # pylint: disable=unused-argument
    # startup
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
main_app.include_router(
    api_router,
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
