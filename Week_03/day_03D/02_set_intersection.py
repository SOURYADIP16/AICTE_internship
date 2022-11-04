''' 
 # © 2022 RuggedBOARRD. - All Rights Reserved. Permission to use, modify, copy, and distribute
 # this source code, object code, or executable code (collectively, Software), is granted only
 # under the terms of a valid written license agreement with RuggedBOARD. Unauthorized copying
 # or other use of the Software is strictly prohibited.  Software is owned by and constitutes
 # the proprietary works, trade secrets, and copyrights of Embitel or its licensors.
 # For further information, contact community.ruggedboard.com / info@ruggedboard.com
 #
 # Application: 02_set_intersection.py
 # Brief:  Write a Python program to create an intersection of sets.
 # Author: SOURYADIP GHOSH ( souryadipghosh62@gmail.com )
 # Title: Project Engineer ruggedBoard.
 # Last Modified Date: 19.10.2022
 #
'''

setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx & sety
print(setz)
