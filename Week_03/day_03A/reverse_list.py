''' 
 # © 2022 RuggedBOARRD. - All Rights Reserved. Permission to use, modify, copy, and distribute
 # this source code, object code, or executable code (collectively, Software), is granted only
 # under the terms of a valid written license agreement with RuggedBOARD. Unauthorized copying
 # or other use of the Software is strictly prohibited.  Software is owned by and constitutes
 # the proprietary works, trade secrets, and copyrights of Embitel or its licensors.
 # For further information, contact community.ruggedboard.com / info@ruggedboard.com
 #
 # Application: reverse_list.py
 # Brief:  Program to reverse List element.
 # Author: SOURYADIP GHOSH ( souryadipghosh62@gmail.com )
 # Title: Project Engineer ruggedBoard.
 # Last Modified Date: 19.10.2022
 #
'''

# Reversing a list  
def Reverse(lst):
	new_lst = lst[::-1]
	return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
