stacks = int(input("Enter an integer from one to eight to determine pyramid height: "))

if stacks <= 0 :
    print("Invalid integer")
elif stacks == 1 :
    print("#")
elif stacks == 2 :
    print(" #\n##")
elif stacks == 3 :
    print("  #\n ##\n###")
elif stacks == 4 :
    print("   #\n  ##\n ###\n####")
elif stacks == 5 :
    print("    #\n   ##\n  ###\n ####\n#####")
elif stacks == 6 :
    print("     #\n    ##\n   ###\n  ####\n #####\n######")
elif stacks == 7 :
    print("      #\n     ##\n    ###\n   ####\n  #####\n ######\n#######")
elif stacks == 8 :
    print("       #\n      ##\n     ###\n    ####\n   #####\n  ######\n #######\n########")
elif stacks >= 9 :
    print("Integer invalid")
