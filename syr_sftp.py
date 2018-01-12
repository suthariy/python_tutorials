#pycrypto
#paramiko
#pysftp

import pysftp as sftp

def push_file_to_server():
    s = sftp.Connection(host = '',
                        username='',
                        password='')
    local_path = ""
    remote_path = ""

    s.put(localpath, remote_path )
    s.close()


def pull_file_from_server():
    s= sftp.Connection(host=,
                       password=,
                       username=)
    s.get(remotepath,localpath)
    s.close()