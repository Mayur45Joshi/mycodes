# ItemsInCart = 0
#
# if ItemsInCart != 2 :
#
#     #raise Exception ("Cart value not meet")
#
#     pass
#
# assert (ItemsInCart == 2)
# assert (ItemsInCart == 0)



#try catch block


try:
    with open('mj1.txt' , 'r' ) as reader:
        print(reader.read())
#user defined exception
except:
    print("Exception block")



try:
    with open('mj1.txt' , 'r' ) as reader:
        print(reader.read())
# system throwing exception
except Exception as e:
    print(e)


finally:
    print("must execute line")