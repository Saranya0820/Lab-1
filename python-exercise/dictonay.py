# 3 using keys and indexing, grab the 'hello' from the following dictionaries
print("Using Keys and indexing Grabing Hello in Dictionaries")
print("-----------------------------------------------------")
d1={'simple_key':'hello'}
d2={'k1':{'k2':'hello'}}
d3={'k1':[
        {
            'nest_key':['this is deep',['hello']]
        }
    ]
}
print(d1['simple_key'])

print(d2['k1']['k2'])

s2=d3['k1'][0]
s2=string['nest_key']
s3 = s2[1]
print(''.join(s3))
