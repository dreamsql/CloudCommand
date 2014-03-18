#-*- encoding=utf8 -*-
import util
import random

def gen_login(cmd, end_date):
    """ 启动应用"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = end_date
    cmd.intentAction = 'com.pada.padasf.LoginActivity'

def gen_pay(cmd, end_date):
    """充值界面"""
    cmd.cloudAction = util.JUMP_ACTION
    cmd.trigger = util.IMMEDIATELY_EXECUTE_TRIGGER
    cmd.validTime = end_date
    cmd.intentAction = 'com.pada.payaction'
    cmd.intentUri = 'pada://padasf/pay?tab=%d' % random.choice([0,1,2])

