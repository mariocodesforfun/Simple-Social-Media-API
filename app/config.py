from pydantic import BaseSettings


# class Settings(BaseSettings):
#     database_hostname: str = "localhost"
#     database_port: str = "5432"
#     database_password: str = "franci2011"
#     database_name: str = "fastapi"
#     database_username: str = "postgres"
#     secret_key: str = "094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
#     algorithm: str = "HS256"
#     access_token_expire_minutes: int = 30

#     class Config:
#         env_file = ".env"

class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str 
    database_password: str
    database_name: str 
    database_username: str 
    secret_key: str 
    algorithm: str 
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"



settings = Settings()