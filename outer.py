from database import Database

d = Database('amaksia',load=False)
d.create_table('cars',['model','cost'],[str,int])
d.create_table('kanapedes',['derma','cost'],[str,int])
d.create_table('carparts',['model','parts'],[str,str])
d.insert('cars',['audi tt','10000'])
d.insert('cars',['bmw x5','30000'])
d.insert('cars',['106rallye','3000'])
d.insert('cars',['cupra','15000'])
d.insert('cars',['cupra','15500'])

d.insert('carparts',['cupra','timoni'])
d.insert('carparts',['cupra','kathismata'])
d.insert('carparts',['drill','kathismata'])
d.insert('carparts',['drill','xeroulia portas'])
d.insert('carparts',['drill','othoni'])
d.insert('carparts',['drill','anapsiktika'])