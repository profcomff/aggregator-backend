from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/timetable/by_group')
def get_timetable_by_group(group: int = Query(..., description="Group number")):
    title: str = 'math'
    audience: int = 502
    teacher: str = '0'
    return [(title, audience, teacher, group)]
