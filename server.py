# -*- coding: utf-8 -*-


from dadmatools.models.normalizer import Normalizer
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Request




class RequestItem(BaseModel):
    text:str



app = FastAPI()


@app.post("/normalize")
async def clean_text(model:RequestItem):
    
    normalizer = Normalizer(
    full_cleaning=False,
    unify_chars=True,
    refine_punc_spacing=True,
    remove_extra_space=True,
    remove_puncs=True,
    remove_html=True,
    remove_stop_word=True,
    replace_number_with=None,
    replace_url_with="",
    replace_mobile_number_with=None,
    replace_emoji_with="",
    replace_home_number_with=None
    )
    text = normalizer.normalize(text=model.text)
    return {"text":text}





@app.get("/")
async def home():
    return "normalizer server is ready"