import logging
from logging.handlers import TimedRotatingFileHandler

# 로그 포맷 설정
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# 로그 파일 이름 설정
LOG_FILE = f'logs/log.log'

# 로거 생성
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# TimedRotatingFileHandler를 사용하여 매일 새로운 로그 파일 생성
handler = TimedRotatingFileHandler(filename=LOG_FILE, when='midnight', interval=1, backupCount=20, encoding="UTF-8")
handler.suffix = "-%Y%m%d-%H%M%S"
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(handler)


