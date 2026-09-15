from __future__ import annotations

from dataclasses import dataclass

from automated_documentation_sync.storage.repositories import DuplicateRecordError, InMemoryRepository

from .sync_states import SyncState


@dataclass(frozen=True)
class SyncCheckpoint:
    run_id: str
    state: SyncState
    source_version_id: str | None = None
    change_set_id: str | None = None
    artifact_hash: str | None = None


class CheckpointRepository:
    """Provider-neutral immutable storage for the latest canonical SYNC checkpoint."""

    def __init__(self) -> None:
        self._records = InMemoryRepository[SyncCheckpoint]()

    def add(self, checkpoint: SyncCheckpoint) -> None:
        self._records.add(checkpoint.run_id, checkpoint)

    def get(self, run_id: str) -> SyncCheckpoint | None:
        return self._records.get(run_id)

    def replace(self, checkpoint: SyncCheckpoint) -> None:
        if self.get(checkpoint.run_id) is None:
            raise KeyError(checkpoint.run_id)
        self._records._records[checkpoint.run_id] = checkpoint


__all__ = ["CheckpointRepository", "SyncCheckpoint"]