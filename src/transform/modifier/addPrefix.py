# -*- coding: utf-8 -*-

# 给某个字段增加前缀
# Author: Alex
# Created Time: 2017年05月16日 星期二 16时45分04秒


class Transform:
    """
    给某个字段增加前缀
    - type: modifier
      name: addPrefix
      field: name_hash
      prefix: 'u.'
    """

    def __init__(self):
        pass

    def do(self, rows, config):
        for row in rows:
            row[config['field']] = config['prefix'] + row[config['field']]
        return rows