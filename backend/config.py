from pydantic_settings import BaseSettings, SettingsConfigDict

class Environment(BaseSettings):
	DATABASE_URL: str

	model_config = SettingsConfigDict(env_file='.env')


config = Environment()
