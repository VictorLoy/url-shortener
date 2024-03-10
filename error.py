from fastapi import HTTPException


def raiseError(statusCode,message):
    raise HTTPException(status_code=statusCode, detail=message)
