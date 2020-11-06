nom1=input("enter the nominee name 1 : ")
nom2=input("enter the nominee name 2 : ")
nom1_votes=0
nom2_votes=0

voter_id=[1,2,3,4,5,6,7,8,9,10]

num_of_voter=len(voter_id)

while True:
    if voter_id==[]:
        print("voting session over")
        if nom1_votes>nom2_votes:
           percent=(nom1_votes/num_of_voter)*100
           print(nom1,"has won","with",percent,"% votes")
           break
        elif nom2_votes>nom1_votes:
             percent=(nom2_votes/num_of_voter)*100
             print(nom2,"has won","with",percent,"% votes")
             break
        elif nom2_votes==nom1_votes:
             print("vote becomes tie \n congratulations both")
             break
    else:
        voter=int(input("enter your voter id number : "))
        if voter in voter_id:
           print("you are a voter")
           voter_id.remove(voter)
           vote=int(input("enter your vote 1 or 2 : "))
           if vote==1:
              nom1_votes+=1
              print("thank you for casting your vote")
           elif vote==2:
                nom2_votes+=1
                print("thank you for casting your vote")
           else:
                print("please enter the valid number")
        else:
             print("your are not a voter here or you have already voted")
