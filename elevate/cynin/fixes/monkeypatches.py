def getAdminUser(portal):
    from AccessControl.SecurityManagement import noSecurityManager
    from AccessControl.SecurityManagement import newSecurityManager
    ## use cynin's siteadmin which is a real plone user instead of admin
    #adminUser = portal.getParentNode().acl_users.getUserById('admin')
    adminUser = portal.acl_users.getUserById('siteadmin')
    print "MONKEY admin user siteadmin"
    newSecurityManager(None,adminUser)
