from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    MIN_AVAILABLE_ENERGY: Optional[int] = 100
    SLEEP_BY_MIN_ENERGY: Optional[list[int]] = [1800, 2400]

    ADD_TAPS_ON_TURBO: Optional[int] = 2500

    AUTO_UPGRADE: Optional[bool] = True
    MAX_LEVEL: Optional[int] = 20

    BALANCE_TO_SAVE: Optional[int] = 1000000
    UPGRADES_COUNT: Optional[int] = 10

    APPLY_DAILY_ENERGY: Optional[bool] = True
    APPLY_DAILY_TURBO: Optional[bool] = True

    RANDOM_TAPS_COUNT: Optional[list[int]] = [10, 50]
    SLEEP_BETWEEN_TAP: Optional[list[int]] = [1, 3]

    USE_RANDOM_USERAGENT: Optional[bool] = False

    USE_PROXY_FROM_FILE: Optional[bool] = False


settings = Settings()
