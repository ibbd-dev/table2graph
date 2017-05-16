# -*- coding: utf-8 -*-

# 将宽表转化为图关系数据
# Author: Alex
# Created Time: 2017年05月16日 星期二 14时14分06秒


class Transform:
    """
    配置样例：
    - expand: graph
      relationships:
      - fromField: name
        toField: name
        isAttr: true
        relationship: name
      - fromField: name
        toField: age
        toType: Int
        isAttr: true
        relationship: age
      - fromField: friend
        toField: friend
        isAttr: true
        relationship: name
      - fromField: name
        toField: friend
        relationship: friend
    """
    # 属性允许的数据类型
    toTypes = ['string', 'int', 'float', 'double', 'boolean', 'date', 'dateTime', 'geojson']

    def __init__(self):
        pass

    def do(self, rows, config):
        data = []
        for row in rows:
            for relation in config['relationships']:
                res = {
                    'from': row[relation['fromField']],
                    'to': row[relation['toField']],
                    'relationship': relation['relationship'],
                }

                res['from'] = u"<%s>" % res['from']
                res['relationship'] = u"<%s>" % res['relationship']
                if 'isAttr' in relation and relation['isAttr']:
                    if 'toType' in relation:
                        res['to'] = u"\"%s\"%s" % (res['to'], self._parseType(relation['toType']))
                    else:
                        res['to'] = u"\"%s\"" % res['to']
                else:
                    res['to'] = u"<%s>" % res['to']

                data.append([u"%s\t%s\t%s\t." % \
                            (res['from'], res['relationship'], res['to'])])

        return data

    def _parseType(self, to_type):
        """
        to_type: to字段的类型，支持如下值:
            string
            int
            float
            double
            boolean
            date
            dateTime
            geojson
        """
        if to_type == 'geojson':
            return '^^<geo:geojson>'
        return '^^<xs:%s>' % to_type