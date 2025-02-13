class Solution(object):
    def hammingWeight(self, n):
  
        binary = bin(n)[2:]
      #  print(len(binary)) 
        count = 0

        for a in binary:
            print("a " +  a)
            if int (a) == 1:
                count+=1
                print("count " + str(count))
        return count
