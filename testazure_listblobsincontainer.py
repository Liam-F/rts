# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 16:36:56 2015

@author: justin.malinchak
"""


# List blobs in container
from azure.storage.blob import BlobService
blob_service = BlobService(account_name='portalvhdss5m831rhl98hj', account_key='Z1MliCYE7p9Ks9kYQoGeM4V99hODtiJL82BVi/zIm06jLYh7n0tV8YaZHzITKixMwUUmjJ1Vp05XrgHG+gXFlg==')

blobs = []
marker = None
while True:
    batch = blob_service.list_blobs('mycontainer', marker=marker)
    blobs.extend(batch)
    if not batch.next_marker:
        break
    marker = batch.next_marker
for blob in blobs:
    bname = blob.name
    print('')
    print(bname)
    print('')
    bpathname = 'C:\\Batches\\$Work\\' + bname
    blob_service.get_blob_to_path('mycontainer', bname, bpathname)
    print('')
    print('blob downloaded ' + bpathname)
    print('')