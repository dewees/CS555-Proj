'''
CS555 Project
Zero-Knowledge Subgraph Isomorphism
Members:
    Craig West
    Max DeWees
    David Hersh
    Michael Kouremetis
'''

import os
import hashlib
'''
    parameters: random1List = 2D list of random values in int/string values - use random.getrandbits() as uses mersenne twister
            random2List = 2D list of random values in int/string values - use random.getrandbits() as uses mersenne twister
            bitList = 2D list of bits in int/string values aka the matrix
'''
def bitCommit_HASH_SHA1_list( random1List, random2List, bitList ):
    commitments = []
    for idx, row in enumerate(bitList):  #iterating through row of matrix
        rowOut=[]
        for idx1, val in enumerate(row): #iterating through col of matrix
            temp = random1List[idx][idx1] + random2List[idx][idx1] + str(bitList[idx][idx1])
            rowOut.append(hashlib.sha1(temp).hexdigest())
        commitments.append(rowOut)
    return commitments

'''
    Commitment function follows the scheme: H(Random-1, Random-2, Bit), Random-2
    This function is a non-interactive scheme, Alice creates both randoms, does not wait for Bob to send randoms
    parameters:  bitList = 2D list of bits in int/string values, aka the matrix
             randSize = in bytes, the size of the random values used for the commitment
    Note: the Matrix passed must be of form row size = column size ; or else function will blow up
'''
def bitCommit_HASH_SHA1_list_bo(bitList, randSize):
    randMatrix1= getRandMatrix(len(bitList), randSize)
    randMatrix2=getRandMatrix(len(bitList), randSize)
    commitments = []
    for idx, row in enumerate(bitList):  #iterating through row of matrix
        rowOut=[]
        for idx1, val in enumerate(row): #iterating through col of matrix
            temp = randMatrix1[idx][idx1] + randMatrix2[idx][idx1] + str(val)
            rowOut.append(hashlib.sha1(temp).hexdigest())
        commitments.append(rowOut)
    out = []
    out.append(commitments)
    out.append(randMatrix1)
    out.append(randMatrix2)
    return out    # returns [commitments, 1st set of randoms, 2nd set of randoms] - a bit commit to send would be
                      # [commitments, 1st set of randoms]  OR [commitments, 2nd set of randoms]


'''
    returns a 2D matrix of random value for the bit commitment, this function is called by bitCommit_HASH_SHA1_list_bo()
    parameters: size = row size(or column size) or matrix will be committing to
            randValueSize = the size(in bits) of the random values used in the commitment
'''
def getRandMatrix(size, randValueSize):
    rand= []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(os.urandom(randValueSize))
        rand.append(row)
    return rand
