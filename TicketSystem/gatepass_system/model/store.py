from datetime import datetime
from http.client import HTTPResponse
from typing import List, Optional

from gatepass_system.enum.PassStatus import PassStatus
from gatepass_system.model.GatePass import GatePass
from gatepass_system.service.CreateGatePass import CreateGatePass


class GatePassStore:
    def __init__(self) -> None:
        self._gate_passes: List[GatePass] = []
        self._next_id: int = 1

    def create(self, data: CreateGatePass) -> GatePass:
            new_pass = GatePass(
                id=self._next_id,
                visitor_name=data.visitor_name,
                visitor_phone=data.visitor_phone,
                host_name=data.host_name,
                status=PassStatus.PENDING,
                created_at=datetime.now().isoformat(timespec="seconds"),
            )
            self._gate_passes.append(new_pass)
            self._next_id += 1
            return new_pass

    def list(self, status: Optional[PassStatus] = None) -> List[GatePass]:
        if status is None:
            return list(self._gate_passes)
        return [gp for gp in self._gate_passes if gp.status == status]

    def get(self, pass_id: int) -> Optional[GatePass]:
        # Returns the GatePass object or None
        return next((gp for gp in self._gate_passes if gp.id == pass_id), None)

    def delete(self, pass_id: int) -> bool:
            gate_pass = self.get(pass_id)
            if gate_pass is None:
                return False
            self._gate_passes.remove(gate_pass)
            return True


store = GatePassStore()