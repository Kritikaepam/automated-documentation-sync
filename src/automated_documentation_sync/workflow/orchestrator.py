from __future__ import annotations

from .checkpoint_repository import CheckpointRepository, SyncCheckpoint
from .sync_states import SyncState, validate_transition


class DuplicateRunError(ValueError):
    """Raised when a run is started more than once."""


class SyncOrchestrator:
    def __init__(self, repository: CheckpointRepository | None = None) -> None:
        self.repository = repository or CheckpointRepository()

    def start_run(self, run_id: str, *, source_version_id: str | None = None) -> SyncCheckpoint:
        if not run_id:
            raise ValueError("run_id is required")
        if self.repository.get(run_id) is not None:
            raise DuplicateRunError(run_id)
        checkpoint = SyncCheckpoint(
            run_id=run_id,
            state=SyncState.INGESTED,
            source_version_id=source_version_id,
        )
        self.repository.add(checkpoint)
        return checkpoint

    def transition(
        self,
        run_id: str,
        target: SyncState,
        *,
        change_set_id: str | None = None,
        artifact_hash: str | None = None,
    ) -> SyncCheckpoint:
        current = self.repository.get(run_id)
        if current is None:
            raise KeyError(run_id)
        validate_transition(current.state, target)
        checkpoint = SyncCheckpoint(
            run_id=current.run_id,
            state=target,
            source_version_id=current.source_version_id,
            change_set_id=change_set_id or current.change_set_id,
            artifact_hash=artifact_hash or current.artifact_hash,
        )
        self.repository.replace(checkpoint)
        return checkpoint

    def resume(self, run_id: str) -> SyncCheckpoint:
        checkpoint = self.repository.get(run_id)
        if checkpoint is None:
            raise KeyError(run_id)
        return checkpoint


__all__ = ["DuplicateRunError", "SyncOrchestrator"]