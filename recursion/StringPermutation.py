def permute(s):
    out = []

    #Base Case
    if len(s) == 1:
        out = [s]
    
    else:
        #for every letter in string

        for i,let in enumerate(s):
            # For every permutation from step 2 and 3
            print("this is i statement -> " + str(i))
            
            for perm in permute( s[:i] + s[i+1: ]):
                print("this is letter statement -> " + let)
                print("this is perm statement -> " + perm)
                #Add it to the output
                out += [let+perm]
                print("this is out statement -> " + str(out))

    return out


print(permute('abc'))