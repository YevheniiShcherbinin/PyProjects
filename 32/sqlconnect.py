import configparser
import mysql.connector
import numpy as np
import sshtunnel

config = configparser.ConfigParser()
config.read('config.ini')


def database():
    with sshtunnel.SSHTunnelForwarder(ssh_address_or_host=config['mysqlDB']['ssh_address_or_host'],
                                      ssh_username=config['mysqlDB']['ssh_username'],
                                      ssh_pkey=config['mysqlDB']['ssh_pkey'],
                                      remote_bind_address=config['mysqlDB']['remote_bind_address'],
                                      ) as tunnel:
        cnx = mysql.connector.MySQLConnection(user=config['mysqlDB']['user'],
                                              password=config['mysqlDB']['password'],
                                              host=config['mysqlDB']['host'],
                                              database=config['mysqlDB']['database'],
                                              port=config['mysqlDB']['port'])
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM vottelo_dev.users;')
    arr = np.array(cursor.fetchall())
    cursor.close()
    cnx.close()
