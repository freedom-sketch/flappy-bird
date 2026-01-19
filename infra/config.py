from pydantic import BaseModel
import json

class Application(BaseModel):
    title: str = "App"
    icon_path: str = ""
    menu_background_path: str = ""
    width: int = 300
    height: int = 300

class Config(BaseModel):
    application: Application = Application()
    
    @classmethod
    def from_json_file(cls, file_path: str):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return cls(**data)