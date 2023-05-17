from typing import Union
import pyrebase
import json
from pams_crawling import get_user_info
from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver

app = FastAPI()

with open("auth.json") as f:
    config = json.load(f)

@app.get("/pams/{urlnum}")
async def read_user_me(urlnum:str):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    try:
        basicInfo_list, schoolAct_list, clubAct_list, volunteer_list, extraAct_list = await get_user_info(urlnum)
    except Exception as e:
        return {'fail the crawling'}

    name = basicInfo_list[1]

    #기본정보 저장
    basic_dict = {"상태":basicInfo_list[0], "학번":basicInfo_list[2], "전공":basicInfo_list[3], "학년":basicInfo_list[4]}
    db.child("users").child(name).child("기본정보").set(basic_dict)

    #교내활동 저장
    if schoolAct_list[0] == "조회된 정보가 없습니다.":
        db.child("users").child(name).child("교내활동").set("조회된 정보가 없습니다.")
    else:
        for i in range(0, int(len(schoolAct_list)/5)):
            info = {"활동유형":schoolAct_list[(5 * i) + 0], "활동명":schoolAct_list[(5 * i) + 1], "운영기간":schoolAct_list[(5 * i) + 2], "운영부서":schoolAct_list[(5 * i) + 3], "수상":schoolAct_list[(5 * i) + 4]}
            db.child("users").child(name).child("교내활동").child(i).set(info)

    #학생단체 활동 이력
    if clubAct_list[0] == "조회된 정보가 없습니다.":
        db.child("users").child(name).child("학생단체활동").set("조회된 정보가 없습니다.")
    else:
        for i in range(0, int(len(clubAct_list)/4)):
            info = {"구분":clubAct_list[(4 * i) + 0], "단체명":clubAct_list[(4 * i) + 1], "활동기간":clubAct_list[(4 * i) + 2], "직책":clubAct_list[(4 * i) + 3]}
            db.child("users").child(name).child("학생단체활동").child(i).set(info)

    #봉사활동 저장
    if volunteer_list[0] == "조회된 정보가 없습니다.":
        db.child("users").child(name).child("봉사활동").set("조회된 정보가 없습니다.")
    else:
        for i in range(0, int(len(volunteer_list)/6)):
            info = {"구분":volunteer_list[(6 * i) + 0], "봉사활동명":volunteer_list[(6 * i) + 1], "봉사기간":volunteer_list[(6 * i) + 2], "봉사시간":volunteer_list[(6 * i) + 3], "봉사장소":volunteer_list[(6 * i) + 4], "확인기관":volunteer_list[(6 * i) + 5]}
            db.child("users").child(name).child("봉사활동").child(i).set(info)

    #대외활동 저장
    if extraAct_list[0] == "조회된 정보가 없습니다.":
        db.child("users").child(name).child("대외활동").set("조회된 정보가 없습니다.")
    else:
        for i in range(0, int(len(extraAct_list)/4)):
            info = {"대회명":extraAct_list[(4 * i) + 0], "대회기간":extraAct_list[(4 * i) + 1], "주최기관":extraAct_list[(4 * i) + 2], "수상실적":extraAct_list[(4 * i) + 3]}
            db.child("users").child(name).child("대외활동").child(i).set(info)
