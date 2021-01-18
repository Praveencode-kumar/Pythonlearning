# =============================================================================
# 
# '''Write a function called sed that takes as arguments a pattern string, a replacement
# string, and two filenames; it should read the first file and write the contents into the second file
# (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
# with the replacement string.
# 14.6. Databases 137
# If an error occurs while opening, reading, writing or closing files, your program should catch the
# exception, print an error message, and exit. '''
# =============================================================================


def sed_pattern(pat,rep,rfile,wfile):
    try:
        r=open(rfile)
        w=open(wfile,'w')
        a='a'
        text=''
        while a != '':
            a=r.readline()
            text+=a
        while pat in text:
            p=text.find(pattern)
            text=text[:p]+rep+text[p+len(pat):]
        w.write(text)
        r.close()
        w.close()
    except:
        return 'file not found'
