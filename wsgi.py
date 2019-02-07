'''
아파치 서버가 이 파일을 구동하여 flask 가동시킴
여기서는 Flask 객체를 가져와서 참조
'''
import sys 
import os

# 경로 설정
CUR_DIR = os.getcwd()
#에러의 출력방향과 일반 출력 방향 설정
sys.stdout = sys.stderr
#path 추가( 시스템 가동위치(현재위치) 잡음)
sys.path.insert(0, CUR_DIR)

#서버 가져오기
#run.py의 app = Flask 객체 올림
from run import app as application