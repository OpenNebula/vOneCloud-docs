.. _authentication:

==============
Authentication
==============

By default, the authentication of vOneCloud is an internal user/password system, with user and group information stored in an internal database. 

You want to pull your users from other source? No problem! vOneCloud supports a variety of authentication methods that can be configured.

LDAP Authentication
--------------------

When enabled, vOneCloud will connect to an already running LDAP server and retrieve information about a user that is trying to login. If this user is authenticated and is the first time vONeCloud sees her, it can place her on a particular group or set of groups depending on LDAP attributes. Read more `here <http://docs.opennebula.org/4.10/administration/authentication/ldap.html#active-directory>`__.

Active Directory Authentication
-------------------------------

Have a corporate Active Directory? vOneCloud can `use it too <http://docs.opennebula.org/4.10/administration/authentication/ldap.html#active-directory>`__!.

X509 Authentication
-------------------

Want to strenght your cloud infrastructure security? This is the `right choice for you <http://docs.opennebula.org/4.10/administration/authentication/x509_auth.html#x509-auth>`__.

SSH Authentication
------------------

When enabled, users will generate login tokens based on standard ssh rsa keypairs for authentication. Check `this guide <http://docs.opennebula.org/4.10/administration/authentication/ssh_auth.html#ssh-auth>`__ for more information.
