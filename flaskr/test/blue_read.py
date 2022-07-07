# -*- coding: utf-8 -*
import configparser
from flask import Blueprint
blue_read = Blueprint('blue_read',__name__)
@blue_read.route('/blue_read')
def new_blue_read():
    conf = configparser.ConfigParser()
    conf.read("config.conf",encoding='utf8')
    lianjieshu = conf.get("mysql", "lianjie")
    daxiaoshu = conf.get("mysql", "daxiao")
    with open("config.txt", "a+") as f:
        f.write(lianjieshu + "\n")
        f.write(daxiaoshu + "\n")
        f.close()
    return "success"