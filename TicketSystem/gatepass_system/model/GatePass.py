from typing import Optional

from gatepass_system.service.CreateGatePass import CreateGatePass
from gatepass_system.enum.PassStatus import PassStatus


class GatePass(CreateGatePass):
    # What the server stores and returns - adds server-controlled fields.

    id: int
    status: PassStatus = PassStatus.PENDING
    created_at: str
    check_in_time: Optional[str] = None
    # check_out_time: Optional[str] = None
