import math

print("Enter the number of tolerance needed: ")
X=int(input())

def Nominal_Dim(dim,Tolpos,Tolneg):

    
    if dim<0:
       Nom_dim=(dim+dim+Tolneg-Tolpos)/2
       linear_max=round((dim+Tolneg),2)
       linear_min=round((dim+Tolpos),2)
       linear_max_list.append(linear_max)
       linear_min_list.append(linear_min)
       
    else:
        Nom_dim=(dim+dim+Tolpos-Tolneg)/2
        linear_max=round((dim+Tolpos),2)
        linear_min=round((dim-Tolneg),2)
        linear_max_list.append(linear_max)
        linear_min_list.append(linear_min)
        
        
    return Nom_dim

def Variance(Tolpos,Tolneg):
    sigma=(Tolpos+Tolneg)/(k*2)
    return sigma

## def Linear_Max_Min(Nom_dim,sigma):
    ## linear_max=Nom_dim+(k*sigma)
    ## linear_min=Nom_dim-(k*sigma)
    ## linear_max_list.append(linear_max)
    ## linear_min_list.append(linear_min)



print("Enter sigma Value :")
k=float(input())
print("Sigma multiplier is K ",k)

Nom_dim_list=[]
sigma_list=[]
Variance_list=[]
linear_max_list=[]
linear_min_list=[]


for i in range(X):
    print("Enter the dim,Tol,-Tol : ")
    dim=float(input())
    Tolpos=float(input())
    Tolneg=float(input())
    sigma=Variance(Tolpos,Tolneg)
    sigma_list.append(sigma)
    Variance_list.append(sigma*sigma)
    Nom_dim=Nominal_Dim(dim,Tolpos,Tolneg)
    Nom_dim_list.append(Nom_dim)
    
    
Total_Nominal_Dim=sum([x for x in Nom_dim_list])
linear_max_total=sum([x for x in linear_max_list])
linear_min_total=sum([x for x in linear_min_list])
Total_Variance=sum([x for x in Variance_list])
Contribution=[round((x/Total_Variance*100),1) for x in Variance_list]        
     
Rss=math.sqrt(Total_Variance)
print("Total Variance i", Total_Variance)
print("RSS Variance is ",Rss)


print("Total mean is :",Total_Nominal_Dim)
print("Stat Max is :",Total_Nominal_Dim+(Rss*k))   
print("Stat Min is :",Total_Nominal_Dim-(Rss*k))
print(linear_max_list)   
print("Linear max is ",linear_max_total)
print(linear_min_list)
print("Linear min is",linear_min_total)
for i in Contribution:
    print(i)











