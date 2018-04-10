#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:XiaoYang
import pymongo

c = pymongo.MongoClient()
client = c['bin']
db = client['test']
# print(list(db.find({'class':{'$eq':30.0}})))
# db.insert({'class':'爬虫','students':60})
# db.update({'class':'爬虫'},{'$set':{'students':50}})
# db.delete_one({'students':50})
print(list(db.find()))