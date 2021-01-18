
# =============================================================================
# 
# Exercise 14.4. In a large collection of MP3 files, there may be more than one copy of the same song,
# stored in different directories or with different file names. The goal of this exercise is to search for
# duplicates.
# 
# =============================================================================


def files(dirf):
    import os 
    mlist=[]
    for x,y,z in os.walk(dirf):
        if len(z)>0:
            for i in z:
                if i[-1]=='3':
                    mlist.append(x+'/'+i)
    return mlist