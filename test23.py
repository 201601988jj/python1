myList=[1,8,3,4,2,7]

print('현재 리스트 : %s' %myList)
myList.append(80)
print("append(80)후의 리스트 :%s"% myList)

print("pop()으로 추출한 값 :%s" % myList.pop(0))
print("pop()후의 리스트 :%s" %myList)

myList.reverse()
print("reverse()후의 리스트 : %s" %myList)

myList.sort()
print("sort()후의 리스트:%s" %myList)
print("2값의 위치 :%d " %myList.index(2))
myList.reverse()
print("reverse()후의 리스트 : %s" %myList)

print("2값의 위치 :%d " %myList.index(2))

myList.insert(2,222)
print("insert(2,222 후의 리스트: %s " %myList)

myList.remove(222)
print("remove(222) 후의 리스트: %s " %myList)

myList.extend([70,80,90])
print("extend(70,80,90])후의 리스트: %s " %myList)

print("70값의 개수: ")