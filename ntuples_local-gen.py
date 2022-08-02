import json

f = open("path_recid.txt", "r")
lines = f.readlines()
f.close()
size=len(lines)

variables=[]
for i in range(0, size):
    aux=lines[i].split()
    variables.append([aux[0], int(aux[1]), aux[2] ])

def findRecid(recid):
    result=" "
    for j in range(0,size):
        if(recid==variables[j][0]):
            result= variables[j]    
    return result

data = {}
data['data'] =  {}
data['ttbar'] = {}
data['single_top_t_chan'] = {}
data['single_atop_t_chan'] = {}
data['single_top_tW'] = {}
data['wjets'] =  {}

#24119
data['data']['single muon'] = {}
data['data']['single muon']['file']=[]
data['data']['single muon']['file'].append({
    'path': findRecid("24119")[2],
    'ntrees': findRecid("24119")[1]
})
data['data']['single muon']['ntrees_total']=findRecid("24119")[1]
#24120
data['data']['single electron'] = {}
data['data']['single electron']['file']=[]
data['data']['single electron']['file'].append({
    'path': findRecid("24120")[2],
    'ntrees': findRecid("24120")[1]
})
data['data']['single electron']['ntrees_total']=findRecid("24120")[1]

#19980
data['ttbar']['nominal']={}
data['ttbar']['nominal']['file']=[]
data['ttbar']['nominal']['file'].append({
    'path': findRecid("19980")[2],
    'ntrees': findRecid("19980")[1]
})
data['ttbar']['nominal']['ntrees_total']=findRecid("19980")[1]

#19983
data['ttbar']['scaledown']={}
data['ttbar']['scaledown']['file']=[]
data['ttbar']['scaledown']['file'].append({
    'path': findRecid("19983")[2],
    'ntrees': findRecid("19983")[1]
})
data['ttbar']['scaledown']['ntrees_total']=findRecid("19983")[1]

#19985
data['ttbar']['scaleup']={}
data['ttbar']['scaleup']['file']=[]
data['ttbar']['scaleup']['file'].append({
    'path': findRecid("19985")[2],
    'ntrees': findRecid("19985")[1]
})
data['ttbar']['scaleup']['ntrees_total']=findRecid("19985")[1]

#19949
data['ttbar']['ME_var']={}
data['ttbar']['ME_var']['file']=[]
data['ttbar']['ME_var']['file'].append({
    'path': findRecid("19949")[2],
    'ntrees': findRecid("19949")[1]
})
data['ttbar']['ME_var']['ntrees_total']=findRecid("19949")[1]

#19999
data['ttbar']['PS_var']={}
data['ttbar']['PS_var']['file']=[]
data['ttbar']['PS_var']['file'].append({
    'path': findRecid("19999")[2],
    'ntrees': findRecid("19999")[1]
})
data['ttbar']['PS_var']['ntrees_total']=findRecid("19999")[1]

#19397
data['single_top_t_chan']['nominal'] = {}
data['single_top_t_chan']['nominal']['file']=[]
data['single_top_t_chan']['nominal']['file'].append({
    'path': findRecid("19397")[2],
    'ntrees': findRecid("19397")[1]
})
data['single_top_t_chan']['nominal']['ntrees_total']=findRecid("19397")[1]

#19407
data['single_atop_t_chan']['nominal'] = {}
data['single_atop_t_chan']['nominal']['file']=[]
data['single_atop_t_chan']['nominal']['file'].append({
    'path': findRecid("19407")[2],
    'ntrees': findRecid("19407")[1]
})
data['single_atop_t_chan']['nominal']['ntrees_total']=findRecid("19407")[1]

#19419
data['single_top_tW']['nominal'] = {}
data['single_top_tW']['nominal']['file']=[]
data['single_top_tW']['nominal']['file'].append({
    'path': findRecid("19419")[2],
    'ntrees': findRecid("19419")[1]
})

#19412
data['single_top_tW']['nominal']['file'].append({
    'path': findRecid("19412")[2],
    'ntrees': findRecid("19412")[1]
})
data['single_top_tW']['nominal']['ntrees_total']= findRecid("19419")[1]+findRecid("19412")[1]

#20548
data['wjets']['nominal'] = {}
data['wjets']['nominal']['file']=[]
data['wjets']['nominal']['file'].append({
    'path': findRecid("20548")[2],
    'ntrees': findRecid("20548")[1]
})
data['wjets']['nominal']['ntrees_total']=findRecid("20548")[1]

with open('data.json', 'w') as file:
    json.dump(data, file)
