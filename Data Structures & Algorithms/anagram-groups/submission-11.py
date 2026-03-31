class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        histogram_dict = {}
        final_list = []

        for s in strs:
            letter_count = [0] * 26
            for ch in s:
                letter_count[ord(ch) - 97] += 1
                
            letter_count_s = ""
            for i,num in enumerate(letter_count):
                print(letter_count_s)
                letter_count_s += chr(i)+str(num)
   
            if letter_count_s in histogram_dict.keys():
                histogram_dict[letter_count_s].append(s)
            else:
                histogram_dict[letter_count_s] = [s]


        for key in histogram_dict:
            final_list.append(histogram_dict[key])  

        print(histogram_dict)
        return final_list             


            



                