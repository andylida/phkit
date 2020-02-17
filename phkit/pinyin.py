#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/17
"""
### pinyin
汉字转为拼音，拼音分为音调和非音调两块。

拼音为字母+数字形式，例如pin1。
"""
from pypinyin import lazy_pinyin, Style
import re

# 音调：5为轻声
_diao_re = re.compile(r"([12345]$)")


def han2pinyin(han, errors=None):
    """
    汉语文本转为拼音列表
    :param han: str,汉语文本字符串
    :param errors: function,对转拼音失败的字符的处理函数，默认保留原样
    :return: list,拼音列表
    """
    if errors is None:
        errors = "default"
    pin = lazy_pinyin(han, style=Style.TONE3, errors=errors, strict=True)
    return pin


def split_pinyin(py):
    """
    单个拼音转为音素列表
    :param py: str,拼音字符串
    :param errors: function,对OOV拼音的处理函数，默认保留原样
    :return: list,音素列表
    """
    parts = _diao_re.split(py)
    if len(parts) == 1:
        fuyuan = py
        diao = "5"
    else:
        fuyuan = parts[0]
        diao = parts[1]
    return [fuyuan, diao]


if __name__ == "__main__":
    print(__file__)
    assert han2pinyin("拼音") == ['pin1', 'yin1']
    assert han2pinyin("汉字,a1") == ['han4', 'zi4', ',a1']