# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# Author:           wangkun
# Created:          2021/5/5
# Description:      this file contains logger
# ------------------------------------------------------------------
import os
import json
import logging.config
 
class Logger_Hanlder():
    """
    the logger
    """
    def __init__(self):
        pass
 
    @classmethod
    def setup_logging(cls,default_path=r"../src/log.json", report_path = None, default_level=logging.INFO, env_key="LOG_CFG"):
        """
        default_path: log config json 文件路径, 默认为 r"../src/log.json", 从example库中执行的路径
        report_path: log 日志文件输出 的目录路径
        default_level: log 默认的输出级别
        env_key:  环境变量
        """
        logger = logging.getLogger('logs:%s.py' %__name__)
 
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, "r") as f:
                config = json.load(f)
                cls.config_json = config
 
                if report_path is not None:
                    if not os.path.exists(report_path):
                        os.makedirs(report_path)
                    for handler in config['handlers'].values():
                        if 'filename' in handler:
                            handler['filename'] = os.path.join(report_path,handler['filename'])
                logging.config.dictConfig(config)
 
        else:
            logging.basicConfig(level=default_level)
        return logger

mylogger = Logger_Hanlder.setup_logging(report_path='./logs')
 
if __name__ == '__main__':
    logger = Logger_Hanlder.setup_logging(report_path='./logs')
    logger.info("INFO：LOG STARTTING >>>>>>>>>>>>>>> ",)
    logger.error("INFO：LOG STARTTING >>>>>>>>>>>>>>> ", )
