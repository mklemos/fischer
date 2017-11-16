from __future__ import unicode_literals
from treelib import Tree, Node

SystemTree = Tree()
SystemTree.create_node("System", "System") # Root Node

#Network Folder
SystemTree.create_node("Network Folder", "Network Folder",  parent="System")
SystemTree.create_node("Increase Quota to 250MB", parent="Network Folder")
SystemTree.create_node("Increase Quota to 500MB", parent="Network Folder")
SystemTree.create_node("Increase Quota to 1GB", parent="Network Folder")
SystemTree.create_node("Increase Quota to 2.5GB", parent="Network Folder")
SystemTree.create_node("Increase Quota to 5GB", parent="Network Folder")
SystemTree.create_node("Increase Quota to 10GB", parent="Network Folder")
SystemTree.create_node("Increase Quota to 12.5GB", parent="Network Folder")
SystemTree.create_node("Increase Quota to 25GB", parent="Network Folder")
SystemTree.create_node("Increase Quota to 100GB", parent="Network Folder")

#Offical Website
SystemTree.create_node("Official Website", "Official Website", parent="System")

SystemTree.create_node("Create website", "Create website", parent="Official Website")
SystemTree.create_node("Official website", parent="Create website")

SystemTree.create_node("Add a developer", "Add a developer", parent="Official Website")
SystemTree.create_node("Provides developer", parent="Add a developer") #A sudo leaf node to make sure the parrent is a subtree and has a child

SystemTree.create_node("Create MySQL accounts", "Create MySQL accounts", parent="Official Website")
SystemTree.create_node("MySQL Account - Prod", parent="Create MySQL accounts")
SystemTree.create_node("MySQL Account - Dev Server", parent="Create MySQL accounts")

SystemTree.create_node("Reset website permissions", "Reset website permissions", parent="Official Website")
SystemTree.create_node("Production Website - Permission Reset", parent="Reset website permissions")


#Personal Website
SystemTree.create_node("Personal website", "Personal Website", parent="System")
SystemTree.create_node("Personal website - MySQL", parent="Personal Website")

#Departmental Email Account
SystemTree.create_node("Departmental Email Account", "Departmental Email Account", parent="System")
SystemTree.create_node("Departmental Email Account", parent="Departmental Email Account") #Leaf node for the check

#Test
SystemTree.create_node("Test", "Test", parent="System")
SystemTree.create_node("Test Role", parent="Test")
SystemTree.create_node("TestRole2", parent="Test")

#IT Admin
SystemTree.create_node("IT Admin", "IT Admin", parent="System")
SystemTree.create_node("Google Apps - Admin", parent="IT Admin")
SystemTree.create_node("Active Directory - Admin", parent="IT Admin")
SystemTree.create_node("LDAP bnd Account", parent="IT Admin")

SystemTree.show(line_type="ascii-em")