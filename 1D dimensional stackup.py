import math

print("Enter the number of tolerance needed: ")
X=int(input())

def Mean_Tolerance(dim,Tolpos,Tolneg):
    if dim<0:
       mean_dim=(dim+dim+Tolneg-Tolpos)/2
    
    else:
        mean_dim=(dim+dim+Tolpos-Tolneg)/2
    return mean_dim

def Variance(Tolpos,Tolneg):
    sigma=(Tolpos+Tolneg)/4/2

    return sigma

def Linear_Max_Min(mean_dim,sigma):
    linear_max=mean_dim+(sd*sigma)
    linear_min=mean_dim-(sd*sigma)
    linear_max_list.append(linear_max)
    linear_min_list.append(linear_min)




print("Enter sigma Value :")
sd=float(input())

mean_dim_list=[]
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
    mean_dim=Mean_Tolerance(dim,Tolpos,Tolneg)
    mean_dim_list.append(mean_dim)
    Linear_Max_Min(mean_dim,sigma)
    
Total_Mean_Tolerance=sum([x for x in mean_dim_list])
linear_max_total=sum([x for x in linear_max_list])
linear_min_total=sum([x for x in linear_min_list])
Total_Variance=sum([x for x in Variance_list])
Contribution=[round((x/Total_Variance*100),1) for x in Variance_list]        
     
Rss=math.sqrt(Total_Variance)
print("Total Variance i", Total_Variance)
print("RSS Variance is ",Rss)


print("Total mean is :",Total_Mean_Tolerance)
print("Stat Max is :",Total_Mean_Tolerance+(Rss*sd))   
print("Stat Min is :",Total_Mean_Tolerance-(Rss*sd))   
print("Linear max is ",linear_max_total)
print("Linear min list",linear_min_total)
for i in Contribution:
    print(i)
    










