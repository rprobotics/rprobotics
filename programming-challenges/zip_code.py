#!/usr/bin/env python














# while local <= len(zip_range_collection):
#     # need to establish if either range[0] or range[1] is in the middle
#     # or if range[0] is smaller than lower, AND range[1] is larger than upper
#     upper = zip_range_collection[local][1]
#     lower = zip_range_collection[local][0]
#
#     # if range[0] is in the middle
#     if lower < range[0] < upper:
#         #print(zip_range_collection[local])
#         new_lower = lower
#         if range[1] < upper:
#             new_upper = upper
#         else:# upper < range[1]:
#             new_upper = range[1]
#         new_zip_range_collection.remove(range)
#         new_zip_range_collection.remove([new_lower, new_upper])
#
#         return find_overlap([new_lower, new_upper], new_zip_range_collection, counter)
#     # if range[1] is in the middle
#     # if we end up here, we've established range[0] is not in the middle
#     elif lower < range[1] < upper:
#         new_lower = range[0]
#         new_upper = upper
#         try:
#             new_zip_range_collection.remove(range)
#         except:
#             pass
#         try:
#             new_zip_range_collection.remove([new_lower, new_upper])
#         except:
#             pass
#         return find_overlap([new_lower, new_upper], new_zip_range_collection, counter)
#     # if
#     elif range[0] < lower and upper < range[1]:
#
#         new_lower = range[0]
#         new_upper = range[1]
#         try:
#             new_zip_range_collection.remove(range)
#         except:
#             pass
#         try:
#             new_zip_range_collection.remove([new_lower, new_upper])
#         except:
#             pass
#
#         return find_overlap([new_lower, new_upper], new_zip_range_collection, counter)
#     elif lower > range[0] < upper and upper > range[1] > lower:
#         new_lower = range[0]
#         new_upper = upper
#         try:
#             new_zip_range_collection.remove(range)
#         except:
#             pass
#         try:
#             new_zip_range_collection.remove([new_lower, new_upper])
#         except:
#             pass
#         #print('hisi')
#         # zip_ranges = ([94133, 94133], [94200, 94299], [94600, 94699], [94100, 94799], [94100, 94599])  # , [10000, 99999])
#         return find_overlap([range[0], upper], new_zip_range_collection, counter)
#
#     else:
#         new_lower = range[0]
#         new_upper = range[1]
#         try:
#             new_zip_range_collection.remove(range)
#         except:
#             pass
#         #return find_overlap([new_lower, new_upper], new_zip_range_collection, counter)
#         return [new_lower, new_upper]
#
#     local += 1
# return range
# #return [new_lower, new_upper]


# def find_overlap(range, zip_range_collection):
#     """
#
#
#     :param range:
#     :param zip_range_collection:
#     :return:
#     """
#
#     local = 0
#     new_zip_range_collection = []
#     while local < len(zip_range_collection):
#         # need to establish if either range[0] or range[1] is in the middle
#         # or if range[0] is smaller than lower, AND range[1] is larger than upper
#         upper = zip_range_collection[local][1]
#         lower = zip_range_collection[local][0]
#         if lower == range[0] and upper == range[1]:
#             local += 1
#             pass
#         # if range[0] is in the middle
#         if lower < range[0] < upper:
#             #print(zip_range_collection[local])
#             new_lower = lower
#             if lower < range[1] < upper:
#                 new_upper = upper
#             elif upper < range[1]:
#                 new_upper = range[1]
#
#         # if range[1] is in the middle
#         # if we end up here, we've established range[0] is not in the middle
#         elif lower < range[1] < upper:
#             new_lower = range[0]
#             new_upper = upper
#         elif range[0] < lower and upper < range[1]:
#             new_lower = range[0]
#             new_upper = range[1]
#         #elif range[0] == range[1]:
#         #    return [range[0], range[1]]
#         else:
#             new_lower = range[0]
#             new_upper = range[1]
#             return [new_lower, new_upper]
#             #return [lower, upper]
#
#         local += 1
#     #return [new_lower, new_upper]

#
#
# def find_overlap(range, zip_range_collection, new_zip_range_collection):
#     print(new_zip_range_collection)
#     local = 0
#     counter = zip_range_collection.index(range)
#     while local <= len(new_zip_range_collection):
#
#
#
#

def clean_range(range, zip_range_collection):
    try:
        zip_range_collection.remove([range[0], range[1]])
        return zip_range_collection
    except:
        pass
    finally:
        return zip_range_collection



def minimize_ranges(zip_range_collection, new_zip_range_collection):
    zip_range_collection = list(zip_range_collection)
    for counter,i in enumerate(zip_range_collection):
        zip_range_collection.remove(i)
        local = 0
        i_lower = i[0]
        i_upper = i[1]
        if len(new_zip_range_collection) == 0:
            return minimize_ranges(zip_range_collection, [[i_lower, i_upper]])
        else:
            while local <= counter:
                lower = new_zip_range_collection[local][0]
                upper = new_zip_range_collection[local][1]
                if i_lower < lower < i_upper:
                    new_lower = i_lower
                    if upper > i_upper:
                        new_upper = upper
                    else:
                        new_upper = i_upper
                    new_zip_range_collection = clean_range([i_lower, i_upper], new_zip_range_collection)
                    new_zip_range_collection = clean_range([lower, upper], new_zip_range_collection)
                    new_zip_range_collection.append([new_lower, new_upper])
                    break
                elif i_lower < upper < i_upper:
                    new_upper = upper
                    if lower < i_lower:
                        new_lower = lower
                    else:
                        new_lower = i_lower
                    new_zip_range_collection = clean_range([i_lower, i_upper], new_zip_range_collection)
                    new_zip_range_collection = clean_range([lower, upper], new_zip_range_collection)
                    new_zip_range_collection.append([new_lower, new_upper])
                    local = 0
                    break
                    #return minimize_ranges(zip_range_collection, new_zip_range_collection)
                #elif i_lower
                else:
                    new_zip_range_collection.append(i)
                    #new_zip_range_collection.append([new_lower, new_upper])
                    #return minimize_ranges(zip_range_collection, new_zip_range_collection)
                    #break
                local += 1
        print(new_zip_range_collection)







if __name__ == '__main__':
    zip_ranges = ([94133, 94133], [94131, 94140], [94130, 94133], [94200, 94299], [94600, 94699], [94100, 94399], [93990, 94599])  # , [10000, 99999])
    #zip_ranges = ([94133, 94133], [94130, 94299])
    print(minimize_ranges(zip_ranges, []))
    #find_overlap(zip_ranges)
















# def cleanup(zip_range_collection):
#     new_zip_range_collection = []
#     for counter,range in enumerate(zip_range_collection):
#         local_counter = 0
#         while local_counter < len(zip_range_collection):
#             if type(zip_range_collection[local_counter][0]) == list:
#                 for i in zip_range_collection[local_counter]:
#                     if i == range:
#                         zip_range_collection.remove(i)
#             local_counter += 1
#     print(zip_range_collection)
