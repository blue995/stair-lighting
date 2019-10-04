import json
import logging
from pathlib import Path

logger = logging.getLogger()

class StairSettingsEntry:
    def __init__(self, *args, **kwargs):
        self.number = -1 if not ('number' in kwargs) else kwargs['number']
        self.gpio = -1 if not ('gpio' in kwargs) else kwargs['gpio']

class StairSettings:
    def __init__(self, *args, **kwargs):
        stairs_raw_json = [] if not ('stairs' in kwargs) else kwargs['stairs']
        self.stairs = []
        for stair_raw_json in stairs_raw_json:
            tmp_stairs_entry = StairSettingsEntry(**stair_raw_json)
            self.stairs.append(tmp_stairs_entry)

class StairConfig:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
    
    @property
    def settings(self) -> StairSettings:
        self.read_settings()
        return self._settings

    def read_settings(self):
        if not self.file_path.exists():
            self.init_settings()
        logger.debug('Reading config from: {file} '.format(file=self.file_path))
        with open(self.file_path, 'r') as f:
            settings_as_dict = json.load(f)
            settings = StairSettings(**settings_as_dict)
            self._settings = settings

    def init_settings(self):
        if self.file_path.exists():
            logger.debug('{file} found.'.format(file=self.file_path))
            return
        logger.debug('{file} not found. Initializing with default settings.'.format(file=self.file_path))
        self.settings = StairSettings()

    @settings.setter
    def settings(self, new_settings: StairSettings):
        settings_as_dict = new_settings.__dict__
        with open(self.file_path, 'w') as f:
            json.dump(settings_as_dict, f)
        self.read_settings()
