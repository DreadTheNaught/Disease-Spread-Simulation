import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random

def Create_Random_SI(transmission_chance = 0.6, number_of_people = 50, connections_per_person = 5, connection_chance = 0.2):
    
    g = nx.newman_watts_strogatz_graph(number_of_people,connections_per_person,connection_chance)
    nx.set_node_attributes(g,"S","status")
    g.nodes[0]["status"] = "I"

    t = 0
    def update(t):

        #Plotting stuff
        node_color = [] 
        for node in g.nodes(data=True):
            if 'S' in node[1]['status']:
                node_color.append('blue')

            elif 'I' in node[1]['status']:
                node_color.append('red')

        my_pos = nx.spring_layout(g, seed = 100)
        nx.draw(g, pos = my_pos, with_labels=True, node_color=node_color, node_size=400, edge_color='black', linewidths=1, font_size=10)

        infected_nodes = []
        for node in g.nodes(data=True): #Parses through all the nodes
            if "I" in node[1]['status']:
                infected_nodes.append(node[0]) #Appends node to list if node is infected

        for infected_node in infected_nodes: #Parses through infected nodes
                neighbours = list(g.neighbors(infected_node)) #Gets list of neighbours of infected node
                for neighbour in neighbours: #Parses through neighbours of infected nodes
                    if random.random() < transmission_chance: #Checks for a random chance
                        g.nodes[neighbour]['status'] = 'I' #Infects neighbouring node

    fig, ax = plt.subplots()
    ani = anim.FuncAnimation(fig, update, frames=100, interval=1000)
    plt.show()