def MinMaxScaler1(x):
  x_min=112019
  x_max=29122022
  for i in range(len(x)):
    x[i]=(x[i]-x_min)/(x_max-x_min)
  return x
def MinMaxScaler2(x):
  x_min=49
  x_max=999886073 
  for i in range(len(x)):
    x[i]=(x[i]-x_min)/(x_max-x_min)
  return x
def compute_hash(s):
  p = 131;
  m = 10**9 + 9;
  hash_value = 0;
  p_pow = 1;
  for c in s:
      if (c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        x=c.lower()
      else:
        x=c
      hash_value = (hash_value + (ord(x)+1) * p_pow) % m;
      p_pow = (p_pow * p) % m;
  return hash_value;
def convert_date(date):
  newDate=[]
  for i in date:
    splitted_list=i.split('/')
    s=''
    for j in splitted_list:
      s+=j
    newDate.append(int(s))
  return newDate