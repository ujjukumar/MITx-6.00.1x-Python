'''
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''

def oddTuples2(aTup):
    '''
    Another way to solve the problem.
 
    aTup: a tuple
     
    returns: tuple, every other element of aTup. 
    '''
    #  slicing by 2 to achieve the same result
    return aTup[::2]