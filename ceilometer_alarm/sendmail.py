# Authors: Bing Li <libing863@fiberhome.com>
#          Blue <yllan@fiberhome.com>
"""Send Mail for alarm notifier."""

import smtplib
from email.mime.text import MIMEText
from pylsy import pylsytable

from ceilometer.alarm import notifier
from oslo_config import cfg
from ceilometer.openstack.common import log

LOG = log.getLogger(__name__)

MAIL_OPTS = [
    cfg.StrOpt('mail_user',
               default='yllan',
               help='The mail sent from which user.'
               ),
    cfg.StrOpt('user_password',
               default='1qaz2wsx#EDC',
               help='The password of mail sender.'
               ),
    cfg.StrOpt('mail_server',
               default='smtp.fiberhome.com',
               help='The server of mail sender.'
               ),
    cfg.StrOpt('mail_postfix',
               default='fiberhome.com',
               help='The postfix of mail sender.'
               ),
    cfg.ListOpt('to_list',
               default=['libing863@fiberhome.com'],
               help='The user list who the mail will send to.'
               ),
    cfg.BoolOpt('enable',
                default=True,
                help='Whether to send mail when '
                'calling alarm notifier action.'
                ),
]

cfg.CONF.register_opts(MAIL_OPTS, group="alarm_send_mail")

cfg.CONF.import_group('alarm_send_mail', 'ceilometer.service')

class SendMailAlarmNotifier(notifier.AlarmNotifier):

    @staticmethod
    def alarm_send_mail_method(subject, content):
        alarm_send_mail_conf = cfg.CONF.alarm_send_mail
        mail_user = alarm_send_mail_conf.mail_user
        user_password = alarm_send_mail_conf.user_password
        mail_server = alarm_send_mail_conf.mail_server
        mail_postfix = alarm_send_mail_conf.mail_postfix
        to_list = alarm_send_mail_conf.to_list

        mail_from = "Alarm" + "<" + mail_user + "@" + mail_postfix + ">"
        msg = MIMEText(content, _subtype='plain')
        msg['Subject'] = subject
        msg['From'] = mail_from
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP()
            server.connect(mail_server)
            server.login(mail_user, user_password)
            server.sendmail(mail_from, to_list, msg.as_string())
            server.close()
            LOG.info("Send mail successfully!")
            return True
        except Exception, e:
            LOG.error("Send mail failed!")
            return False

    @staticmethod
    def format_content(data):
        attributes = ["Alarm_ID", "Name", "State", "Priority", "Reason"]
        table = pylsytable(attributes)

        Alarm_ID = data.get('alarm_id')
        Name = data.get('alarm_name')
        State = data.get('current')
        Priority = data.get('severity')
#        Alarm_condition = data.get('reason_data')
        Reason = data.get('reason')

        table.add_data("Alarm_ID", Alarm_ID)
        table.add_data("Name", Name)
        table.add_data("State", State)
        table.add_data("Priority", Priority)
#        table.add_data("Alarm_condition", Alarm_condition)
        table.add_data("Reason", Reason)

        return str(table)