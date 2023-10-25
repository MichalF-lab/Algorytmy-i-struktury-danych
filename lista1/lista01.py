import random
import numpy

# Przygotowanie tablic do testów

main_table = numpy.arange(random.randint(5,7))

for item in main_table:
    main_table[item] = float(random.randint(1,100))

# # Funkcja pomocnicza
# def swap(table, a, b):
#    print(table," ",a," ",b)
#    temp = table[a]
#    table[a] = table[b]
#    table[b] = temp
#    print(table," ",a," ",b)

# # def insertionsort(table):
# #   for item in range(len(table)):
# #      for Lower_temp in range(item,-1,-1):
# #         # nie porównujemy tych samych elementów
# #         if(item == Lower_temp): continue
# #         print(Lower_temp, " ", item)  
# #         if(table[item] < table[Lower_temp]):
# #            swap(table,item, Lower_temp)
# #            for this_loop in range(Lower_temp,-1,-1):
# #               if(table[Lower_temp] < table[this_loop]):
# #                 swap(table,this_loop, Lower_temp)
# #   return table

# # Funkcja pomocnicza
# def swap_plus(table, a, b, insertionsortpluscount):
#    temp = table[a]
#    table[a] = table[b]
#    table[b] = temp
#    # print(table)
#    insertionsortpluscount += 2
#    return insertionsortpluscount

# # def insertionsortplus(table):
# #   insertionsortpluscount = 0
# #   for item in range(len(table)):
# #      for Lower_temp in range(item,-1,-1):
# #         # nie porównujemy tych samych elementów
# #         if(item == Lower_temp): continue
# #         if(table[item] < table[Lower_temp]):
# #            insertionsortpluscount = swap_plus(table,item, Lower_temp, insertionsortpluscount)
# #            for this_loop in range(Lower_temp,-1,-1):
# #               print(this_loop, table[Lower_temp] , table[this_loop])
# #               if(table[Lower_temp] < table[this_loop]):
# #                 insertionsortpluscount = swap_plus(table,this_loop, Lower_temp, insertionsortpluscount)
# #   return insertionsortpluscount

#-----------------------------------------------------------------------------

def insertionsort(table):
  for item in range(len(table)):
      temp = table[item]
      i = item - 1
      while(temp < table[i] and i >= 0):
         table[i+1] = table[i]
         i-=1
      if(i != item - 1):
         table[i+1] = temp
  return table

def insertionsortplus(table):
  count_e, count_p = 0,0
  for item in range(len(table)):
      temp = table[item]
      i = item - 1
      count_p += 1
      while(temp < table[i] and i >= 0):
         count_p += 1
         table[i+1] = table[i]
         count_e += 1
         i-=1
      if(i != item - 1):
         table[i+1] = temp
         count_e += 1
  return (count_p,count_e)

# print(insertionsortplus(main_table))
#print(insertionsort(main_table))


#------------------------------------------------------------------


def bubblesort(table):
   for item in range(1,len(table)):
      for i in range(len(table)-item,0,-1):
         if(table[i] < table[i-1]):
            table[i], table[i-1] = table[i-1], table[i]
   return table


def bubblesortplus(table):
   count_e, count_p = 0,0
   for item in range(1,len(table)):
      for i in range(len(table)-item,0,-1):
         count_p += 1
         if(table[i] < table[i-1]):
            table[i], table[i-1] = table[i-1], table[i]
            count_e += 2
   return (count_p, count_e)


# print(main_table)
# print(bubblesortplus(main_table))


#------------------------------------------------------------------

def mergesort(table):
   def sort(table_a, table_b):
      #print(table_a," ",table_b)
      index_a, index_b = 0,0
      new_table = numpy.arange(len(table_a) + len(table_b))
      for index in new_table:
         if(index_a == len(table_a)):
            while (index_b < len(table_b)):
               new_table[index] = table_b[index_b]
               index_b += 1
               index += 1
            #print(new_table)
            return new_table
         
         elif(index_b == len(table_b)):
            while (index_a < len(table_a)):
               new_table[index] = table_a[index_a]
               index_a += 1
               index += 1
            #print(new_table)
            return new_table 
          
         if(table_a[index_a] < table_b[index_b]):
            new_table[index] = table_a[index_a]
            index_a += 1
         else:
            new_table[index] = table_b[index_b]
            index_b += 1
      return new_table
   
   if(len(table) == 1): return table
   if(len(table) == 2):
      if(table[1] < table[0]):
         table[0], table[1] = table[1], table[0]
      return table
   middle = len(table) // 2
   return sort(mergesort(table[:middle]), mergesort(table[middle:]))
      

print(main_table)
print(mergesort(main_table))


#print(main_table)
#print(main_table)
# for item in range(len(main_table)):
#     print (item)

# merge sort - n log n