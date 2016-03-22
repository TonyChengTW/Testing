__author__ = 'Tony Cheng'

# Get domain info via libvirt python API.

import libvirt
import sys


def create_connection():
    conn = libvirt.openReadOnly(None)
    if conn == None:
        print 'Failed to open connection to QEMU/KVM'
        sys.exit(1)
    else:
        print '-- Connection is created successfully --'
        return conn


def close_connnection(conn):
    print ''
    try:
        conn.close()
    except:
        print 'Failed to close the connection'
        return 1

    print 'Connection is closed'


def get_domain_info_by_name(conn, name):
    print ''
    print '---- get domain info by name ----'
    try:
        myDom = conn.lookupByName(name)
    except:
        print 'Failed to find the domain with name "%s"' % name
        return 1

    print "Dom id: %d name: %s" % (myDom.ID(), myDom.name())
    print "Dom state: %s" % myDom.state(0)
    print "Dom info: %s" % myDom.info()
    print "memory: %d MB" % (myDom.maxMemory()/1024)
    print "memory status: %s" % myDom.memoryStats()
    print "vCPUs: %d" % myDom.maxVcpus()


def get_domain_info_by_id(conn, id):
    print ''
    print '---- get domain info by ID ----'
    try:
        myDom = conn.lookupByID(id)
    except:
        print 'Failed to find the domain with ID "%d"' % id
        return 1

    print "Domain id is %d ; Name is %s" % (myDom.ID(), myDom.name())


if __name__ == '__main__':
    name1 = "CentOS-6.7-demo4"
    name2 = "notExist"
    id1 = 2
    id2 = 9999
    print "-- Get domain info via libvirt python API --"
    conn = create_connection()
    get_domain_info_by_name(conn, name1)
    get_domain_info_by_name(conn, name2)
    get_domain_info_by_id(conn, id1)
    get_domain_info_by_id(conn, id2)
    close_connnection(conn)