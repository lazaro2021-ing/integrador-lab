
user="lzr"
password="1522"
server="DESKTOP-02KB195\SQLEXPRESS"
database="integrador-lab"
driver="{SQL Server}"
trusted_connection='yes'

connection_string = f""" DRIVER={driver};
                        SERVER={server};
                        DATABASE={database};
                        TRUSTED_CONNECTION={trusted_connection};
                        User Id={user};
                        """