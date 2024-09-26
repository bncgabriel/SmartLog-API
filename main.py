from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from routes import *

smartlog = FastAPI()