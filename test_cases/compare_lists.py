#compare lists

# debugging arrays
# test_lista = [['a', ''], ['b','c'], ['e', ''], ['f', '']]
# test_listb = [['1', ''], ['b','c'], ['2', ''], ['3', '']]
#
# test_samea = [u"a", [u"b", u"c"], u"e", u"f"]
# test_sameb = [u'a', [u'b', u'c'], u'e', u'f']
# test_samec = ['a', ['b','c'], 'e', 'f']

# userpermissionlist and genertedlist are both lists passed in to be compared.
# userpermissionlist is a list we have generated on our own based on known permissions
#
# generatedlist is one that is created by our testing program that will be compared
# to our userpermissionlist
#
# Username is the parameter that defaults to empty, however, when testing specific
# permission sets please specify the permission set username to overload the default
# empty string.
def compare_lists(userpermissionlist, genertedlist, username = ""):
    # Initialize working comparison lists
    extrapermissionfound = []
    missingpermissionfound = []

    # Check if there is an extra permission in generatedlist
    for lista in genertedlist:
        booltest = False
        for listb in userpermissionlist:
            if lista == listb:
                booltest = True
        if booltest == False:
            extrapermissionfound.append(lista)

    # Check if there is an missing permission in generatedlist
    for listb in userpermissionlist:
        booltest = False
        for lista in genertedlist:
            if listb == lista:
                booltest = True
        if booltest == False:
            missingpermissionfound.append(listb)
    # Write to file if there is a missing or extra permission with the name of the
    # user prepended to the file name and return false
    if extrapermissionfound != [] or missingpermissionfound != []:
        failedpermissionfile = open(username + 'failedpermissionfile.txt', 'w')
        for item in extrapermissionfound:
            failedpermissionfile.write("Extra: %s\n" % item)
            print("Extra: %s\n" % item)
        for item in missingpermissionfound:
            failedpermissionfile.write("Missing: %s\n" % item)
            print("Missing: %s\n" % item)
        return False
    # If we reach here we know that we have two lists that match
    print("No Missing or Extra Dropdowns Found")
    return True

#debugging code
#print(compare_lists(test_lista, test_listb))
