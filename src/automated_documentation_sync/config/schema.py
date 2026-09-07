from dataclasses import dataclass
from typing import Any


class ConfigurationError(ValueError):
    """Raised when required configuration is missing or invalid."""


@dataclass(frozen=True)
class ProjectConfiguration:
    week_start_day: str
    time_zone: str
    working_hours: int
    calendar_reference: str

    def __post_init__(self) -> None:
        if not self.week_start_day or not self.time_zone or not self.calendar_reference:
            raise ConfigurationError("Required project calendar configuration is Not Found")
        if self.working_hours not in (8, 9):
            raise ConfigurationError("Project working hours must be 8 or 9")


def require_project_configuration(values: dict[str, Any]) -> ProjectConfiguration:
    required_keys = ("week_start_day", "time_zone", "working_hours", "calendar_reference")
    missing_keys = [key for key in required_keys if values.get(key) in (None, "")]
    if missing_keys:
        raise ConfigurationError("Required project configuration is Not Found")
    return ProjectConfiguration(
        week_start_day=values["week_start_day"],
        time_zone=values["time_zone"],
        working_hours=values["working_hours"],
        calendar_reference=values["calendar_reference"],
    )
