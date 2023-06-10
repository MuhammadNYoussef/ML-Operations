ML-Ops Course App

Testing (test_numSqrt.py & test_app.py)
```
python -m pytest -vv
```
Deploy:
```
uvicorn app:app --reload
```
URL Example (4^5):
```
http://127.0.0.1:8000/sqrt/4/5
```
