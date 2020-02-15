import anki_vector
import csv
import time
import sys
# global scope variables
local_anim_file_name = "AnimDict.txt"
report_file_name = "Differences Report.txt"


def main():
    print("============================== Animation checker Dev tool ==============================")
    print("Index:")
    while True:
        print("Select [1] to check for differences between local and cloud animation lists")
        print("Select [2] to update the local animation list with the cloud animation list")
        print("Select [3] to nope the hell out of here")

        user_select = input()
        if(user_select == '1'):
            compare_animations()
        if(user_select == '2'):
            print("Are you sure? Once this list is replaced you will no longer know if any animations are out of date")
            user_warning = input("y/n ")
            if(user_warning == 'y'):
                list_from_anki = get_anim_list_from_anki()
                update_local_anim_list(list_from_anki)
                print("Updated local animation list: "+local_anim_file_name)
        if(user_select == '3'):
            break

def get_anim_list_from_anki():
    with anki_vector.Robot() as robot:
        return robot.anim.anim_trigger_list

def get_anim_list_local():
    with open('../JackInABots-Vector-Utilities/Dev tools/Animation/'+local_anim_file_name, 'r') as f:
        reader = csv.reader(f)
        returned_list = list(reader)
        #flattern the list of lists so it is only 1 list
        flattened = []
        for sublist in returned_list:
            for val in sublist:
                flattened.append(val)

    return flattened

def update_local_anim_list(list_to_write):
    with open('../JackInABots-Vector-Utilities/Dev tools/Animation/'+local_anim_file_name, 'w') as f:
        for item in list_to_write:
            f.write("%s\n" % item)

def write_report(list_from_anki, list_from_local, difference_list, removed_or_renamed, added_or_renamed, list_from_anki_count, list_from_local_count):
    with open('../JackInABots-Vector-Utilities/Dev tools/Animation/'+report_file_name, 'w') as f:
        f.write("================ Report ================ \n")
        #write the differences found
        f.write("These animations came from the cloud, but are not stored locally: \n")
        for item in difference_list:
            f.write(str(item)+"\n")
        f.write("\n")

        #write the closer inspection
        if(len(removed_or_renamed) != 0): 
            f.write("Upon closer inspection, these animations seem to be either renamed or removed completely: \n")
            for item in removed_or_renamed:
                f.write(str(item))
                f.write("\n")
            f.write("This is based on the fact that these animations appear in the local list but not the cloud list. \n")
            f.write("\n")

        if(len(added_or_renamed) != 0):
            f.write("Upon closer inspection, these animations seem to be either renamed or added: \n")
            for item in added_or_renamed:
                f.write(str(item))
                f.write("\n")
            f.write("This is based on the fact that these animations appear in the cloud list but not the local list. \n")
            f.write("\n")
        
        #display list count data to infer what the changes likely are
        f.write("The number of animations returned from anki = "+str(list_from_anki_count)+" and the number of animations stored locally = "+str(list_from_local_count)+"\n")
        if(list_from_anki_count > list_from_local_count):
            f.write("From this we can infer that there is likely mostly addition changes \n")
        elif(list_from_anki_count < list_from_local_count):
            f.write("From this we can infer that there is likely mostly removal changes \n")
        elif(list_from_anki_count == list_from_local_count):
            f.write("From this we can infer that there is likely mostly rename changes \n")
        f.write("\n")

        #dump the lists from both lists
        f.write("Now we will regurgitate both lists compared in this report so that you may copy and paste the full lists if you wish. \n")
        f.write("This is the full list returned by Anki: \n")
        f.write(str(list_from_anki)+"\n\n")
        
        f.write("This is the full list stored locally: \n")
        f.write(str(list_from_local)+"\n\n")

        f.write("Please refer to the wiki page on the dev tools on what you should do from here.")

def compare_animations():
    #get list from anki
    print("Getting list of animations from Anki...")
    list_from_anki = get_anim_list_from_anki()

    #get local list
    print("Getting list of animations from Anki...")
    list_from_local = get_anim_list_local()

    #check if defferences, report needs to be made if differences true
    if(list_from_anki == list_from_local):
        print("All animations are up to date.")
        time.sleep(3)
    else:
        print("There are differences. Goddamnit. Creating report...")
        #init vars to be used
        difference_list = []
        removed_or_renamed = []
        added_or_renamed = []
        cloud_anim_count = 0
        local_anim_count = 0
        #calculate difference
        difference_list = list(set(list_from_anki) - set(list_from_local))

        #figure out information for report
        for item in difference_list:
            #either renamed or removed
            if(item not in list_from_anki):
                removed_or_renamed.append(item)

            #either renamed or added
            if(item in list_from_anki and item not in list_from_local):
                added_or_renamed.append(item)

        cloud_anim_count = list_from_anki.count(str)
        list_from_anki_count = len(list_from_anki)
        list_from_local_count = len(list_from_local)

        print("================ Report ================")
        #first display the changes detected
        print("These animations came from the cloud, but are not stored locally: ")
        for item in difference_list:
            print(str(item))
        print()
        go_next = input("Press [Enter] to coninue the report:")

        #try and go into specifics on what the changes likely are
        if(len(removed_or_renamed) != 0): 
            print("Upon closer inspection, these animations seem to be either renamed or removed completely: ")
            for item in removed_or_renamed:
                print(str(item))
            print("This is based on the fact that these animations appear in the local list but not the cloud list. \n")

        if(len(added_or_renamed) != 0):
            print("Upon closer inspection, these animations seem to be either renamed or added: ")
            for item in added_or_renamed:
                print(str(item))
            print("This is based on the fact that these animations appear in the cloud list but not the local list. \n")

        go_next = input("Press [Enter] to coninue the report:")

        #display list count data to infer what the changes likely are
        print("The number of animations returned from anki = "+str(list_from_anki_count)+" and the number of animations stored locally = "+str(list_from_local_count))
        if(list_from_anki_count > list_from_local_count):
            print("From this we can infer that there is likely mostly addition changes \n")
        elif(list_from_anki_count < list_from_local_count):
            print("From this we can infer that there is likely mostly removal changes \n")
        elif(list_from_anki_count == list_from_local_count):
            print("From this we can infer that there is likely mostly rename changes \n")
        
        print("Next we will regurgitate both lists compared in this report so that you may copy and paste the full lists if you wish.")
        go_next = input("Press [Enter] to coninue the report:")

        #dump the lists from both lists
        print("This is the full list returned by Anki:")
        print(str(list_from_anki)+"\n")
        
        print("This is the full list stored locally:")
        print(str(list_from_local)+"\n")

        #write report
        print("Writing report...")
        write_report(list_from_anki, list_from_local, difference_list, removed_or_renamed, added_or_renamed, list_from_anki_count, list_from_local_count)
        print("Report saved. You can find this information in "+report_file_name+" for future reference.")

        print("Please refer to the wiki page on the dev tools on what you should do from here.")
        time.sleep(5)

if __name__ == '__main__':
    main()