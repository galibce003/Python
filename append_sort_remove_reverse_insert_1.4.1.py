#Code to add 'horseback riding' to the third position.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2,'horseback riding')  #.insert can add item with a specific position




#Code to remove 'London'
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.remove('London')  #.remove takes out according to value,
                            #while "del" takes out according to index number as well as position.




#Code to add 'Guadalajara' to the end of the list.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append('Guadalajara')  #.append add values to the last of the list




#Code to rearrange the strings in alphabetical order from A to Z.
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()  #.sort reorder the list from smallest to biggest




#Code to switch the order from now Z to A.
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners = winners
z_winners.reverse()  #.reverse flip the order
print(z_winners)
