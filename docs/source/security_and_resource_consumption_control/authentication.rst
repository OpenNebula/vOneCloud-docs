.. _authentication:

==============
Authentication
==============

By default, vOneCloud authentication uses an internal user/password system with user and group information stored in an internal database.

If you want vOneCloud to have your users pulled from a corporate Active Directory, all the needed components are enabled and just an extra configuration step is needed. As requirements, you will need an Active Directory server with support for simple user/password authentication, as well as a user with read permissions in the Active Directory user’s tree.

:ref:`Log into the vOneCloud console <advanced_login>`, and then proceed to fill the following information in ``/etc/one/auth/ldap_auth.conf``:

You will need to change the following values in the configuration file (/etc/one/auth/ldap_auth.conf):

+--------------+---------------------------------------------------------------------------------+
| :user:       | Active Directory user with read permissions in the user’s tree plus the domain. |
+--------------+---------------------------------------------------------------------------------+
| :password:   | password of this user                                                           |
+--------------+---------------------------------------------------------------------------------+
| :host:       | hostname or IP of the Domain Controller                                         |
+--------------+---------------------------------------------------------------------------------+
| :base:       | base DN to search for users.                                                    |
+--------------+---------------------------------------------------------------------------------+
| :user_field: | Set it to "sAMAccountName"                                                      |
+--------------+---------------------------------------------------------------------------------+


You can find more infromation on the integration with Active Directory `in this guide <http://docs.opennebula.org/4.10/administration/authentication/ldap.html#active-directory>`__ .


vOneCloud supports are a variety of other authentication methods that can be configured, follow the links to find the configuration steps needed:

+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
|  `LDAP <http://docs.opennebula.org/4.10/administration/authentication/ldap.html#active-directory>`__             | | vOneCloud will connect to an existing LDAP server and retrieve information  |
|                                                                                                                  | | about a user that is trying to login                                        |
+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `X509 Authentication <http://docs.opennebula.org/4.10/administration/authentication/x509_auth.html#x509-auth>`__ | | Stenght your cloud infrastructure security                                  |
+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `SSH Authentication <http://docs.opennebula.org/4.10/administration/authentication/ssh_auth.html#ssh-auth>`__    | | Users will generate login tokens based on standard ssh rsa keypairs for     |
|                                                                                                                  | | authentication                                                              |
+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
