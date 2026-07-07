from typing import Optional

from gatepass_system.CreateGatePass import CreateGatePass
from gatepass_system.enums.PassStatus import PassStatus


class GatePass(CreateGatePass):
    # What the server stores and returns - adds server-controlled fields.

    id: int
    status: PassStatus = PassStatus.PENDING
    created_at: str
    check_in_time: Optional[str] = None
    # check_out_time: Optional[str] = None
