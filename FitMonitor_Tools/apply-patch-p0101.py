# (C) Copyright 2017 CloudCube Co.

"""
FitMonitor Patch commit log:
http://172.16.100.91/cascade/cascade-dashboard/commits/vB050-patches-p01xx
20171107    add webhook notify method in frontend
            fix Host Detail guage from type percent to short
            remove HostDetail & IPMI2 dashboard
"""

import os
import shutil
import subprocess
import logging
import time

release_version = 'B090'
patch_version = '0101'
logfile = './patch.log'
logging.basicConfig(filename=logfile,
                    level=logging.DEBUG,
                    format='%(asctime)s %(process)d %(name)-4s %(levelname)-4s %(message)s',
                    datefmt='%y-%m-%d %H:%M:%S')

cdvfile = 'public_gen/cdv.txt'
grafana_basedir = '/home/grafana/go/src/github.com/grafana/grafana'
grafana_serverdir = 'bin'
dashboard_jsondir = 'pkg/data/dashboard'
notification_htmldir = 'public_gen/app/features/alerting/partials'


def apply_patch(grafana_basedir, dashboard_jsondir, notification_htmldir, grafana_serverdir):
    _hd_file = 'HostDetail.json'
    _notifi_edit_file = 'notification_edit.html'
    _grafana_server_file = 'grafana-server'

    patch_hd_fullpath = os.path.join('..', dashboard_jsondir, _hd_file)
    hd_fulldir = os.path.join(grafana_basedir, dashboard_jsondir)

    patch_notifi_edit_fullpath = os.path.join('..', notification_htmldir, _notifi_edit_file)
    notification_edit_fulldir = os.path.join(grafana_basedir, notification_htmldir)

    patch_grafanaserver_fullpath = os.path.join('..', grafana_serverdir, _grafana_server_file)
    grafanaserver_fulldir = os.path.join(grafana_basedir, grafana_serverdir)

    logging.info("Checking HostDetail dir: %s" % hd_fulldir)
    logging.info("Checking HostDetail patch file: %s" % patch_hd_fullpath)
    logging.info("Checking Nofi dir: %s" % notification_edit_fulldir)
    logging.info("Checking Nofi patch file: %s" % patch_notifi_edit_fullpath)
    logging.info("Checking grafana-server dir: %s" % grafanaserver_fulldir)
    logging.info("Checking grafana patch file: %s" % patch_grafanaserver_fullpath)

    if os.path.isfile(patch_hd_fullpath) and \
            os.path.isfile(patch_notifi_edit_fullpath) and \
            os.path.isdir(hd_fulldir) and \
            os.path.isdir(notification_edit_fulldir):

        logging.info("copy %s to %s" % (patch_hd_fullpath, hd_fulldir))
        logging.info("copy %s to %s" % (patch_notifi_edit_fullpath,
                                        notification_edit_fulldir))
        logging.info("copy %s to %s" % (patch_grafanaserver_fullpath, grafanaserver_fulldir))

        shutil.copy(patch_hd_fullpath, hd_fulldir)
        shutil.copy(patch_notifi_edit_fullpath, notification_edit_fulldir)
        shutil.copy(patch_grafanaserver_fullpath, grafanaserver_fulldir)
    else:
        logging.error('The path or file does not exist!')
        raise IOError('The path or file does not exist!')
    return 0


def tag_cdv():
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cdvfile_fullpath = os.path.join(grafana_basedir, cdvfile)
    try:
        with open(cdvfile_fullpath, "a") as cdvfile_handler:
            cdvfile_handler.write("%s\tFitMonitor-%s-p%s\n" % (datetime,
                                                             release_version,
                                                             patch_version))
    except:
        logging.error("The cdv file:%s does not exist or can not open" % cdvfile_fullpath)
    logging.info("patch version appended into cdv!")

def stop_grafana():
    check_cmd = '/usr/bin/stat /proc/1/exe | grep systemd | wc -l'
    try:
        output_check = subprocess.check_output(check_cmd, shell=True,
                                               stderr=subprocess.STDOUT)
        check_systemd = output_check.strip()
    except subprocess.CalledProcessError:
        raise SystemError("cloud not run this command: %s" % check_cmd)

    if check_systemd == '0':
        print("systemV/Upstart : stop grafana-server...")
        stop_cmd = 'service grafana-server stop'
        try:
            output_stop = subprocess.check_output(stop_cmd, shell=True,
                                                     stderr=subprocess.STDOUT)
            logging.info("output_stop = %s" % output_stop)
        except subprocess.CalledProcessError:
            raise SystemError("cloud not run this command: %s" % stop_cmd)
        print("output_restart = %s" % output_stop)
    elif check_systemd == '1':
        print("systemd : stop grafana-server...")
        stop_cmd = 'systemctl stop grafana-server'
        try:
            output_stop = subprocess.check_output(stop_cmd, shell=True,
                                                     stderr=subprocess.STDOUT)
            logging.info("output_stop = %s" % output_stop)
        except subprocess.CalledProcessError:
            logging.error("cloud not run this command: %s" % stop_cmd)
            raise SystemError("cloud not run this command: %s" % stop_cmd)
        logging.info("output_stop = %s" % output_stop)
    return 0

def restart_grafana():
    check_cmd = '/usr/bin/stat /proc/1/exe | grep systemd | wc -l'
    try:
        output_check = subprocess.check_output(check_cmd, shell=True,
                                               stderr=subprocess.STDOUT)
        check_systemd = output_check.strip()
    except subprocess.CalledProcessError:
        raise SystemError("cloud not run this command: %s" % check_cmd)

    if check_systemd == '0':
        print("systemV/Upstart : restarting grafana-server...")
        restart_cmd = 'service grafana-server restart'
        try:
            output_restart = subprocess.check_output(restart_cmd, shell=True,
                                                     stderr=subprocess.STDOUT)
            logging.info("output_restart = %s" % output_restart)
        except subprocess.CalledProcessError:
            raise SystemError("cloud not run this command: %s" % restart_cmd)
        print("output_restart = %s" % output_restart)
    elif check_systemd == '1':
        print("systemd : restarting grafana-server...")
        restart_cmd = 'systemctl restart grafana-server'
        try:
            output_restart = subprocess.check_output(restart_cmd, shell=True,
                                                     stderr=subprocess.STDOUT)
            logging.info("output_restart = %s" % output_restart)
        except subprocess.CalledProcessError:
            logging.error("cloud not run this command: %s" % restart_cmd)
            raise SystemError("cloud not run this command: %s" % restart_cmd)
        logging.info("output_restart = %s" % output_restart)
    return 0


def main():
    logging.info("\n++++++++++++++++++++++++++\nBegin to patch FitMonitor....")
    stop_grafana()
    apply_patch(grafana_basedir,
                dashboard_jsondir,
                notification_htmldir,
                grafana_serverdir)
    restart_grafana()
    tag_cdv()
    return 0

if __name__ == '__main__':
    main()

