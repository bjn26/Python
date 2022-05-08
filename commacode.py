import sys
spam=['apples','bananas','tofu','cats']
def list_item(list):
    for item in list:
        if len(list)==1:
            print(list[0])
        elif item!=list[-1]:
            print(item +',',end='')
        else:
            print('and '+list[-1])
list_item(spam)
