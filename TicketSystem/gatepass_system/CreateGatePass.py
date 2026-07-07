from pydantic import BaseModel


class CreateGatePass(BaseModel):
    # What the client must send to request a new gate pass.
    visitor_name: str
    visitor_phone: str
    host_name: str