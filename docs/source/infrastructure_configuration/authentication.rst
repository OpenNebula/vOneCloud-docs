.. _authentication:

==============
Authentication
==============

By default, vOneCloud authentication uses an internal user/password system with user and group information stored in an internal database.

vOneCloud can pull users from a corporate Active Directory, all the needed components are enabled and just an extra configuration step is needed. As requirements, you will need an Active Directory server with support for simple user/password authentication, as well as a user with read permissions in the Active Directory user’s tree.

You will need to access the :ref:`Control Panel <control_panel>` in order to configure the Active Directory support in vOneCloud. After the configuration is done, users that exist in Active Directory can begin using vOneCloud.

Step 1. Configure Active Directory support
--------------------------------------------------------------------------------

Click on the "Configure OpenNebula" button

.. image:: /images/ad_configure_cp.png
    :align: center

In the following screen, select the "Add Active Directory" category

.. image:: /images/configure_ad_button.png
    :align: center

Fill the needed fields following the criteria described in the next table

+-----------------------+-----------------------------------------------------------------------------------+
|     **Attribute**     |                                  **Description**                                  |
+-----------------------+-----------------------------------------------------------------------------------+
| Server Name           | Chosen name for the authentication backend                                        |
+-----------------------+-----------------------------------------------------------------------------------+
| User                  | Active Directory user with read permissions in the user’s tree plus the domain.   |
+-----------------------+-----------------------------------------------------------------------------------+
| Password              | Active Directory user password                                                    |
+-----------------------+-----------------------------------------------------------------------------------+
| Authentication method | Active Directory server authentication method (eg simple)                         |
+-----------------------+-----------------------------------------------------------------------------------+
| Encryption            | simple or simple_tls                                                              |
+-----------------------+-----------------------------------------------------------------------------------+
| Host                  | hostname or IP of the Domain Controller                                           |
+-----------------------+-----------------------------------------------------------------------------------+
| Port                  | port of the Domain Controller                                                     |
+-----------------------+-----------------------------------------------------------------------------------+
| Base Domain           | base hierarchy where to search for users and groups                               |
+-----------------------+-----------------------------------------------------------------------------------+
| Group                 | group the users need to belong to. If not set any user will do                    |
+-----------------------+-----------------------------------------------------------------------------------+
| User Field            | field that holds the user name, if not set 'cn' will be used                      |
+-----------------------+-----------------------------------------------------------------------------------+
| Group Field           | field name for group membership, by default it is 'member'                        |
+-----------------------+-----------------------------------------------------------------------------------+
| User Group Field      | user field that that is in in the group group_field, if not set 'dn' will be used |
+-----------------------+-----------------------------------------------------------------------------------+

.. image:: /images/cp_ad_conf.png
    :align: center

Click on the "Apply Settings" button when done.

Step 2. Restart vOneCloud services
--------------------------------------------------------------------------------

For changes to take effect, you need to restart vOneCloud services and wait for OpenNebula state to be ON.

.. image:: /images/cp_restart_one.png
    :align: center


You can find more infromation on the integration with Active Directory `in this guide <http://docs.opennebula.org/4.10/administration/authentication/ldap.html#active-directory>`__ .

vOneCloud supports are a variety of other authentication methods with advanced configuration, follow the links to find the configuration steps needed (:ref:`Advanced Login <advanced_login>` needed):

+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `X509 Authentication <http://docs.opennebula.org/4.10/administration/authentication/x509_auth.html#x509-auth>`__ | | Stenght your cloud infrastructure security                                  |
+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `SSH Authentication <http://docs.opennebula.org/4.10/administration/authentication/ssh_auth.html#ssh-auth>`__    | | Users will generate login tokens based on standard ssh rsa keypairs for     |
|                                                                                                                  | | authentication                                                              |
+------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
