import pdb

import firewall_addr_model as fam
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.orm import scoping

class DBManager(object):
    def __init__(self, connection=None):
        self.connection = connection

        self.engine = sa.create_engine(self.connection)
        self.DBSession = scoping.scoped_session(
            orm.sessionmaker(
                bind=self.engine,
                autocommit=True
            )
        )

    def session(self):
        return self.DBSession()

    def setup(self):
        # Normally we would add whatever db setup code we needed here.
        # This will for fine for the ORM
        try:
            fam.SAModel.metadata.create_all(self.engine)
        except Exception as e:
            print('Could not initialize DB: {}'.format(e))


connection = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
     'root', 'Abc12345', '127.0.0.1', '3306', 'sdnms_api')

# dbmgr = DBManager('mysql+pymysql://root:Abc12345@127.0.0.1:3306/tonytest')
dbmgr = DBManager(connection)
# pdb.set_trace()
dbmgr.setup()

session = dbmgr.session()
new_addr = fam.FirewallAddressModel(id='5', name='Bob', content='test', interface='test', comment='')

# pdb.set_trace()
session.begin()
session.add(new_addr)
session.commit()
session.close()
