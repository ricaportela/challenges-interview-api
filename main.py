from dataclasses import Field  
from datetime import datetime
from typing import List, Union, Optional

from fastapi import FastAPI
from pydantic.dataclasses import dataclass  # 


#@dataclass
class Vehicle:
    vehicle: str
    brand: str
    year: int
    description: Union[str, None] = None
    # is_sold: Optional[bool] = Field(False, title='Is Sold')    
    created: datetime
    updated: datetime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "vehicle API"}

app.get("/vehicles/", response_model=List[Vehicle])  # 
def get_vehicles():  # 
    return [  # 
        {
            "vehicle": "santana quantum",
            "brand": "volkswagem",
            "year": "1996",
            "description": "bom estado, zerada",
            #"is_sold": "True",
            "created": "01/01/2022",
            "updated": "01/01/2022",

        },
    ]
