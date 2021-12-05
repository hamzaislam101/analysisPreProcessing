
import csv

def create_edges(nodesFile, ratingsFile):
    with open(nodesFile, 'r') as nodes_file:
        with open('edges_created.csv', 'a') as new_csv:
            writer = csv.writer(new_csv,delimiter=",", lineterminator='\n')
            filtered_nodes = (line.replace('\n', '') for line in nodes_file)
                
            ns = csv.reader(filtered_nodes)        
            x=0
            y=0
            with open(ratingsFile, 'r') as ratings_file:
                filtered_ratings = (line.replace('\n', '') for line in ratings_file)
                rs = list(csv.reader(filtered_ratings))
            for node_row in ns:
                    
                
                imdbid = node_row[0]
                
                print(x)
                    #print(filtered_ratings.length)

                if(rs[x][15]):
                    data=[x-1,85855,rs[x][15]]
                    writer.writerow(data)
                if(rs[x][17]):
                    data=[x-1,85856,rs[x][17]]
                    writer.writerow(data)
                if(rs[x][19]):
                    data=[x-1,85857,rs[x][19]]
                    writer.writerow(data)
                if(rs[x][21]):
                    data=[x-1,85858,rs[x][21]]
                    writer.writerow(data)
                x=x+1

                    #for ratings_row in rs:
                        #print(length)
                    #    if imdbid.strip()[3:] == ratings_row[0].strip() or ratings_row[0].strip() in imdbid or ratings_row[0].strip() == imdbid.strip():
                            
                    #        data=[node_row[0],'0-18',ratings_row[15]]
                    #        writer.writerow(data)
                            #data=[node_row[0],'18-30',ratings_row[17]]
                            #writer.writerow(data)
                            #data=[node_row[0],'30-45',ratings_row[19]]
                            #writer.writerow(data)
                            #data=[node_row[0],'45+',ratings_row[21]]
                            #writer.writerow(data)
                            #break


create_edges("nodes.csv","ratings.csv")
print("done")
                    
