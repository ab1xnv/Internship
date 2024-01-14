#!/usr/bin/env python
# coding: utf-8

# In[1]:


frog_pos = list(['G','G','G','-','B','B','B'])
print("-->Enter an integer less that 7")
print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
print(frog_pos)

while True:
    pos = input("Press q to quit else \nEnter position of frog:")
    if pos == 'q':
        print("YOU LOST!")
        break
    pos = int(pos)

    if pos<0 or 6<pos:
        print("Invalid move")
        continue
    if frog_pos[pos] == '-':
        print("Invalid move")
        continue

    if frog_pos[pos] == 'G':
        if (pos + 1) <= 6 and frog_pos[pos + 1] == '-':
            pass
        elif (pos + 2) <= 6 and frog_pos[pos + 2] == '-' and frog_pos[pos + 1] == 'B':
            pass
        else:
            print("Invalid move")
            break
    if frog_pos[pos] == 'B':
        if (pos - 1) >= 0 and frog_pos[pos - 1] == '-':
            pass
        elif (pos - 2) >= 0 and frog_pos[pos - 2] == '-' and frog_pos[pos - 1] == 'G':
            pass
        else:
            print("Invalid move")

    pos2 = 0
    if frog_pos[pos] == 'G':
        if frog_pos[pos + 1] == '-':
            pos2 = (pos+1)
        elif frog_pos[pos + 2] == '-':
            pos2 = (pos+2)
    if frog_pos[pos] == 'B':
        if frog_pos[pos - 1] == '-':
            pos2 = (pos-1)
        elif frog_pos[pos - 2] == '-':
            pos2 = (pos-2)
    frog_pos[pos], frog_pos[pos2] = frog_pos[pos2], frog_pos[pos]

    print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
    print(frog_pos)

    if frog_pos == ['B','B','B','-','G','G','G']:
        print("YOU WIN")
        break


# In[ ]:




