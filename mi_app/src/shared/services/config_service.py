from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from ..constants import (
    APP_CONFIG_FILE,
    BACKUP_DIR,
    CONFIG_DIR,
    DEFAULT_APP_CONFIG,
    DEFAULT_PROGRAMS_CONFIG,
    PROGRAMS_CONFIG_FILE,
)
from ..dataclasses import AppConfig, CycleDetectorConfig, GeneralConfig, ProgramConfig, ProgramsConfig


class ConfigService:
    _instance: "ConfigService" | None = None

    def __new__(cls) -> "ConfigService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return

        CONFIG_DIR.mkdir(exist_ok=True)
        BACKUP_DIR.mkdir(exist_ok=True)

        self.app_config = self._load_app_config()
        self.programs_config = self._load_programs_config()

        self._initialized = True

    # Load/Save helpers
    def _create_backup(self, file_path: Path) -> None:
        if not file_path.exists():
            return
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP_DIR / f"{file_path.stem}_{timestamp}{file_path.suffix}"
        shutil.copy2(file_path, backup_path)

        backups = sorted(BACKUP_DIR.glob(f"{file_path.stem}_*"))
        for old in backups[:-5]:
            old.unlink()

    def _load_app_config(self) -> AppConfig:
        if not APP_CONFIG_FILE.exists():
            config = AppConfig(
                general=GeneralConfig(**DEFAULT_APP_CONFIG["general"]),
                cycle_detector=CycleDetectorConfig(**DEFAULT_APP_CONFIG["cycle_detector"]),
            )
            self._save_app_config(config)
            return config

        with open(APP_CONFIG_FILE, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        return AppConfig(
            general=GeneralConfig(**data.get("general", DEFAULT_APP_CONFIG["general"])),
            cycle_detector=CycleDetectorConfig(**data.get("cycle_detector", DEFAULT_APP_CONFIG["cycle_detector"])),
        )

    def _load_programs_config(self) -> ProgramsConfig:
        if not PROGRAMS_CONFIG_FILE.exists():
            default_programs = [ProgramConfig(**p) for p in DEFAULT_PROGRAMS_CONFIG["programs"]]
            config = ProgramsConfig(programs=default_programs)
            self._save_programs_config(config)
            return config

        with open(PROGRAMS_CONFIG_FILE, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        programs = [ProgramConfig(**p) for p in data.get("programs", [])]
        return ProgramsConfig(programs=programs)

    def _save_app_config(self, config: AppConfig) -> None:
        self._create_backup(APP_CONFIG_FILE)
        with open(APP_CONFIG_FILE, "w", encoding="utf-8") as handle:
            json.dump(config.to_dict(), handle, indent=2, ensure_ascii=False)

    def _save_programs_config(self, config: ProgramsConfig) -> None:
        self._create_backup(PROGRAMS_CONFIG_FILE)
        with open(PROGRAMS_CONFIG_FILE, "w", encoding="utf-8") as handle:
            json.dump(config.to_dict(), handle, indent=2, ensure_ascii=False)

    # Public API
    def get_app_config(self) -> AppConfig:
        return self.app_config

    def update_app_config(self, section: str, payload: Dict[str, Any]) -> None:
        if section == "general":
            self.app_config.general = GeneralConfig(**payload)
        elif section == "cycle_detector":
            self.app_config.cycle_detector = CycleDetectorConfig(**payload)
        else:
            raise ValueError(f"Sección no soportada: {section}")
        self._save_app_config(self.app_config)

    def get_programs_config(self) -> ProgramsConfig:
        return self.programs_config

    def add_program(self, program_data: Dict[str, Any]) -> int:
        programs = self.programs_config.programs
        next_id = max([p.program_id for p in programs], default=0) + 1
        program_data["program_id"] = next_id
        programs.append(ProgramConfig(**program_data))
        self._save_programs_config(self.programs_config)
        return next_id

    def delete_program(self, program_id: int) -> None:
        self.programs_config.programs = [p for p in self.programs_config.programs if p.program_id != program_id]
        self._save_programs_config(self.programs_config)

    def get_program(self, program_id: int) -> Optional[ProgramConfig]:
        for program in self.programs_config.programs:
            if program.program_id == program_id:
                return program
        return None
