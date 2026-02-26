from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/whoami")
async def get_whoami(request: Request):
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        client_ip = forwarded.split(",")[0]
    else:
        client_ip = request.client.host

    return {
        "ip": client_ip,
        "user_agent": request.headers.get("User-Agent"),
        "message": "Conexión exitosa",
    }
