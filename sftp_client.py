#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : sftp_client.py
# Author            : DDAAREN <ddaaren@163.com>
# Date              : 2019.08.18
# Last Modified Date: 2019.08.18
# Last Modified By  : DDAAREN <ddaaren@163.com>

import paramiko
#paramiko.util.log_to_file('/tmp/paramiko.log')
import os
from stat import S_ISDIR

class OutsourcingSftp(object):
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.client = {}
        return

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.user, password=self.password)
        self.client = paramiko.SFTPClient.from_transport(transport)
        return

    def close(self):
        self.client.close()
        return

    def sftp_walk(self, remote_path):
        path = remote_path
        files = []
        folders = []
        for f in self.client.listdir_attr(remote_path):
            if S_ISDIR(f.st_mode):
                folders.append(f.filename)
            else:
                files.append(f.filename)
        if files:
            yield path, files
        for folder in folders:
            new_path = os.path.join(remote_path, folder)
            for x in self.sftp_walk(new_path):
                yield x

    def download(self, remote_path, local_path):
        for path, files in self.sftp_walk(remote_path):
            for f in files:
                new_path = os.path.normpath(local_path+path)
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                self.client.get(os.path.join(path, f), os.path.join(new_path, f))


