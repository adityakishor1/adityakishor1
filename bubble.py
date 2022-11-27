def bubble_sort(elements):
    size = len(elements)
    for i in range(size-1):
      for j in range(size-1):
        if elements[j] > elements[j+1]:
            temp = elements[j]
            elements[j] = elements[j+1]
            elements[j+1]= temp
if __name__=="__main__":
    elements = [5,8,2,9,63,1]
    bubble_sort(elements)
    print(elements)
