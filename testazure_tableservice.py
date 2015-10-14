# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 16:47:26 2015

@author: justin.malinchak
"""

from azure.storage.table import TableService, Entity
table_service = TableService(account_name='portalvhdss5m831rhl98hj', account_key='Z1MliCYE7p9Ks9kYQoGeM4V99hODtiJL82BVi/zIm06jLYh7n0tV8YaZHzITKixMwUUmjJ1Vp05XrgHG+gXFlg==')


table_service.create_table('tasktable')
task = {'PartitionKey': 'tasksSeattle', 'RowKey': '1', 'description' : 'Take out the trash', 'priority' : 200}
table_service.insert_entity('tasktable', task)

task = Entity()
task.PartitionKey = 'tasksSeattle'
task.RowKey = '2'
task.description = 'Wash the car'
task.priority = 100
table_service.insert_entity('tasktable', task)
#
task = {'description' : 'Take out the garbage', 'priority' : 250}
table_service.update_entity('tasktable', 'tasksSeattle', '1', task)
#
task = {'description' : 'Take out the garbage again', 'priority' : 250}
table_service.insert_or_replace_entity('tasktable', 'tasksSeattle', '1', task)

task = {'description' : 'Buy detergent', 'priority' : 300}
table_service.insert_or_replace_entity('tasktable', 'tasksSeattle', '3', task)

task10 = {'PartitionKey': 'tasksSeattle', 'RowKey': '10', 'description' : 'Go grocery shopping', 'priority' : 400}
task11 = {'PartitionKey': 'tasksSeattle', 'RowKey': '11', 'description' : 'Clean the bathroom', 'priority' : 100}
table_service.begin_batch()
table_service.insert_entity('tasktable', task10)
table_service.insert_entity('tasktable', task11)
table_service.commit_batch()

task = table_service.get_entity('tasktable', 'tasksSeattle', '1')
print(task.description)
print(task.priority)

tasks = table_service.query_entities('tasktable', "PartitionKey eq 'tasksSeattle'")
for task in tasks:
    print(task.description)
    print(task.priority)
    
tasks = table_service.query_entities('tasktable', "PartitionKey eq 'tasksSeattle'", 'description')
for task in tasks:
    print(task.description)
    
table_service.delete_entity('tasktable', 'tasksSeattle', '1')
table_service.delete_table('tasktable')
