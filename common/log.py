import os
import logging
import time
import colorlog
from common.conf import BASE_DIR

# 日志颜色配置
log_colors_config = {
    'DEBUG': 'white',  # cyan white
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

# 获取日志记录器
log = logging.getLogger('auto_ui_logger')

# 设置日志级别
log.setLevel(logging.DEBUG)

# 输出到控制台
console_handler = logging.StreamHandler()

# 创建带时间戳的日志文件名
datetime = time.strftime('%Y-%m-%d')  # 使用年月日格式
path = BASE_DIR + '/log/'
if not os.path.exists(path):
    os.makedirs(path)

filename = path + f'/run_log_{datetime}.log'

# 输出到文件
file_handler = logging.FileHandler(
    filename=filename,
    mode='a',
    encoding='utf8'
)

# 日志级别设置
# log和handler以最高级别为准，不同handler之间可以不一样，不相互影响
log.setLevel(logging.DEBUG)
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

# 日志输出格式
file_formatter = logging.Formatter(
    # fmt='[(\s*(asctime)s.\%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
    fmt='[%(levelname)s] [%(asctime)s.%(msecs)03d] : %(message)s %(filename)s -> %(funcName)s line:%(lineno)d',
    datefmt='%Y-%m-%d  %H:%M:%S'
)

console_formatter = colorlog.ColoredFormatter(
    # fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
    fmt='%(log_color)s[%(levelname)s] [%(asctime)s.%(msecs)03d] : %(message)s %(filename)s -> %(funcName)s line:%(lineno)d',
    datefmt='%Y-%m-%d  %H:%M:%S',
    log_colors=log_colors_config
)

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# 重复日志问题处理：
# 1、防止多次addHandler；
# 2、logname保证每次添加的时候不一样；
# 3、显示完log之后调用removeHandler
if not log.handlers:
    log.addHandler(console_handler)
    log.addHandler(file_handler)

console_handler.close()
file_handler.close()

if __name__ == '__main__':
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')