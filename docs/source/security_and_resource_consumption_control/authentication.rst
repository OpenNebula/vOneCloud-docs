.. _authentication:

==============
Authentication
==============

By default, vOneCloud authentication uses an internal user/password system with user and group information stored in an internal database.

If you want to pull your users from other source, vOneCloud supports are a variety of authentication methods that can be configured.

+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
|  `LDAP <http://docs.opennebula.org/4.10/administration/authentication/ldap.html#active-directory>`__             | | vOneCloud will connect to an existing LDAP server and retrieve information  |
|                                                                                                                  | | about a user that is trying to login                                        |
+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `Active Directory <http://docs.opennebula.org/4.10/administration/authentication/ldap.html#active-directory>`__  | | vOneCloud will connect to an existing Active Directory server               |
+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `X509 Authentication <http://docs.opennebula.org/4.10/administration/authentication/x509_auth.html#x509-auth>`__ | | Stenght your cloud infrastructure security                                  |
+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `SSH Authentication <http://docs.opennebula.org/4.10/administration/authentication/ssh_auth.html#ssh-auth>`__    | | Users will generate login tokens based on standard ssh rsa keypairs for     |
|                                                                                                                  | | authentication                                                              |
+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
