graph= {
	'a':['b','c'],
	'b':['d'],
	'c':['e'],
	'd':['f'],
	'e':[],
	'f':[]
}

def DFS(graph,source):
  stack=[source]
  
  while(len(stack)>0):
    current= stack.pop()
    #key operation
    print(current)
    
    for i in graph[current]:
      stack.append(i)#insert(0, i)

def recursive_DFS(graph,source):
  #key operation
  print(source)
  
  for i in graph[source]:
    recursive_DFS(graph,i)


def BFS(graph,source):
	queue=[source]

	while(len(stack)>0):
		current= stack.pop(0)
		#key operation
		print(current)

		for i in  graph[source]:
			queue.append(i)


recursive_DFS(graph,'a')