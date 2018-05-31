import pdb

import firewall_addr_model as fa
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
                autocommit=False
            )
        )

    def session(self):
        return self.DBSession()

    def setup(self):
        # Normally we would add whatever db setup code we needed here.
        # This will for fine for the ORM
        try:
            fa.SAModel.metadata.create_all(self.engine)
        except Exception as e:
            print('Could not initialize DB: {}'.format(e))


connection = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
     'root', 'Abc12345', '127.0.0.1', '3306', 'sdnms_api')

# dbmgr = DBManager('mysql+pymysql://root:Abc12345@127.0.0.1:3306/tonytest')
dbmgr = DBManager(connection)
# pdb.set_trace()
dbmgr.setup()

session = dbmgr.session()

try:
    new_addr_id6 = fa.FirewallAddressModel(id='6', name='Bob6', content='test6', interface='test6', comment='')
    new_addr_id7 = fa.FirewallAddressModel(id='7', name='Bob2', content='test2', interface='test2', comment='')

    # pdb.set_trace()
    # session.begin()
    session.add(new_addr_id6)
    # item1 = session.query(fa.FirewallAddressModel.filter(fa.FirewallAddressModel.id == '5'))
    item2 = session.query(fa.FirewallAddressModel).filter_by(id='6').first()
    item3 = session.query(fa.FirewallAddressModel).get(7).name
    item4 = session.query(fa.FirewallAddressModel).all()
    # Note: (TonyCheng) item3[0].name , len(item3)
    item5 = session.query(fa.FirewallAddressModel).filter_by(id='6').update({"name": "addr6",
                                                                             "interface": "int6"})
    '''                                                                         
    # Batch Insert
    item6 = session.add_all([fa.FirewallAddressModel(id='8', name='wendy', content='Wendy Williams',
                                                     interface='int8', comment=''),
                             fa.FirewallAddressModel(id='9', name='mary', content='Mary Contrary',
                                                     interface='int9', comment=''),
                             fa.FirewallAddressModel(id='10', name='fred', content='Fred Flinstone',
                                                     interface='int10', comment='')])
    '''
    # Order by
    item6 = session.query(fa.FirewallAddressModel).order_by(fa.FirewallAddressModel.id)
    item7 = session.query(fa.FirewallAddressModel).order_by(fa.FirewallAddressModel.id.desc())

    # Delete Record
    # item8 = session.delete(item2)

    # pdb.set_trace()
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()
