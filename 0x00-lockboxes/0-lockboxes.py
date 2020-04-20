#!/usr/bin/python3
"""
Lockboxes
"""

def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    # key_store = []
    # for i in range(len(boxes) - 1):
    #     flag = 0
    #     for j in range(len(boxes[i])):
    #         key_store.append(boxes[i][j])
    #         if boxes[i][j] == i + 1:
    #             flag = 1
    #     if i + 1 in key_store:
    #         continue
    #     if flag == 0:
    #         print(key_store)
    #         print("i: {}".format(i))
    #         return False
    # return True

    # key_store = [key for sublist in boxes for key in sublist]
    # print(key_store)
    # for i in range(len(boxes) - 1):
    #     flag = 0
    #     for j in range(len(boxes[i])):
    #         key_store.append(boxes[i][j])
    #         if boxes[i][j] == i + 1:
    #             flag = 1
    #     if i + 1 in key_store:
    #         continue
    #     if flag == 0:
    #         print("i: {}".format(i))
    #         return False
    # return True

    key_store = [key for sublist in boxes for key in sublist]
    # print(key_store)
    for i in range(len(boxes) - 1):
        if i + 1 in key_store[:i + 1] or i + 1 in key_store[i + 2:]:
            continue
        return False
    return True
