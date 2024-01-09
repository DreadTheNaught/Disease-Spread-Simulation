import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random


def Create_Random_SIR(transmission_chance = 0.6, number_of_people = 50, connections_per_person = 5, connection_chance = 0.2, time_to_recover = 4):
    
    g = nx.newman_watts_strogatz_graph(number_of_people,connections_per_person,connection_chance)
    nx.set_node_attributes(g, "S", "status")


    g.nodes[0]["status"] = "I"
    g.nodes[0]["infectionTime"] = 0

    def update(time):

        #Plotting stuff
        node_color = [] 
        for node in g.nodes(data=True):
            if 'S' in node[1]['status']:
                node_color.append('blue')

            elif 'I' in node[1]['status']:
                node_color.append('red')

            elif 'R' in node[1]['status']:
                node_color.append('white')

        my_pos = nx.spring_layout(g, seed = 100)
        nx.draw(g, pos = my_pos, with_labels=True, node_color=node_color, node_size=400, edge_color='black', linewidths=1, font_size=10)


        infected_nodes = []
        for node in g.nodes(data=True): #Parses through all the nodes
            if "I" in node[1]['status']:
                infected_nodes.append(node[0]) #Appends node to list if node is infected

        for infected_node in infected_nodes: #Parses through infected nodes 
            if (time - g.nodes[infected_node]["infectionTime"]) >= time_to_recover:
                g.nodes[infected_node]["status"] = "R"
                continue
            
            neighbours = list(g.neighbors(infected_node)) #Gets list of neighbours of infected node
            for neighbour in neighbours: #Parses through neighbours of infected nodes
                if (g.nodes[neighbour]['status'] == 'S') and (random.random() < transmission_chance): #Checks for a random chance
                    g.nodes[neighbour]['status'] = 'I' #Infects neighbouring node
                    g.nodes[neighbour]["infectionTime"] = time
        time+=1

    fig, ax = plt.subplots()
    ani = anim.FuncAnimation(fig, update, frames=100, interval=1000, repeat=False, init_func=lambda: None)
    plt.show()