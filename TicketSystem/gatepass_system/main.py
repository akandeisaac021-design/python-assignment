from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException

from gatepass_system.CreateGatePass import CreateGatePass
from gatepass_system.GatePass import GatePass
from gatepass_system.enums.PassStatus import PassStatus
from gatepass_system.store import store

app = FastAPI(title="Gate Pass System")


def _fetch_id(pass_id: int) -> GatePass:
    gate_pass = store.get(pass_id)
    if gate_pass is None:
        raise HTTPException(status_code=404, detail="Gate pass not found")
    return gate_pass


def _require_status(gate_pass: GatePass, expected: PassStatus, action: str) -> None:
    if gate_pass.status != expected:
        raise HTTPException(
            status_code=400,
            detail=f"Only a {expected.value} pass can be {action} (this one is {gate_pass.status.value})",
        )


@app.get("/")
def root():
    return {"message": "Gate Pass System API - visit /docs to try it o ut"}


@app.post("/gatepasses", response_model=GatePass, status_code=201)
def create_gate_pass(data: CreateGatePass):
    # Request a new gate pass. Starts out in 'pending' status
    return store.create(data)


@app.get("/gatepasses", response_model=List[GatePass])
def list_gate_passes(status: Optional[PassStatus] = None):
    # List all gate passes. Optionally filter with ?status=pending etc.
    return store.list(status)


@app.get("/gatepasses/{pass_id}", response_model=GatePass)
def get_gate_pass(pass_id: int):
    return _get_or_404(pass_id)


@app.put("/gatepasses/{pass_id}/approve", response_model=GatePass)
def approve_gate_pass(pass_id: int):
    # The host approves a pending request.
    gate_pass = _get_or_404(pass_id)
    _require_status(gate_pass, PassStatus.PENDING, "approved")
    gate_pass.status = PassStatus.APPROVED
    return gate_pass


@app.put("/gatepasses/{pass_id}/reject", response_model=GatePass)
def reject_gate_pass(pass_id: int):
    """The host rejects a pending request."""
    gate_pass = _get_or_404(pass_id)
    _require_status(gate_pass, PassStatus.PENDING, "rejected")
    gate_pass.status = PassStatus.REJECTED
    return gate_pass


@app.put("/gatepasses/{pass_id}/check-in", response_model=GatePass)
def check_in_gate_pass(pass_id: int):
    # Record the visitor's arrival. Only valid for an approved pass.
    gate_pass = _get_or_404(pass_id)
    _require_status(gate_pass, PassStatus.APPROVED, "checked in")
    gate_pass.check_in_time = datetime.now().isoformat(timespec="seconds")
    return gate_pass


@app.put("/gatepasses/{pass_id}/check-out", response_model=GatePass)
def check_out_gate_pass(pass_id: int):
    # Record the visitor's departure. Only valid after check-in.
    gate_pass = _get_or_404(pass_id)
    if gate_pass.check_in_time is None:
        raise HTTPException(
            status_code=400,
            detail="Cannot check out a visitor who hasn't checked in",
        )
    if gate_pass.check_out_time is not None:
        raise HTTPException(status_code=400, detail="Visitor has already checked out")
    gate_pass.check_out_time = datetime.now().isoformat(timespec="seconds")
    return gate_pass


@app.delete("/gatepasses/{pass_id}")
def delete_gate_pass(pass_id: int):
    if not store.delete(pass_id):
        raise HTTPException(status_code=404, detail="Gate pass not found")
    return {"message": f"Gate pass {pass_id} deleted"}
