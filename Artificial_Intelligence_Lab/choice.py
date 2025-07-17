print("select any two subjects :\n1.physics\n2.chemistry\n3.maths\n4.biology\n5.circuits\n6.electronics\n7.programming\n8.AI concepts\n9.statistics")
sub1=str(input("select first subject name:\n"))
sub2=str(input("select second subject name:\n"))
if(sub1=="physics")and(sub2=="maths")or(sub1=="maths" and sub2=="physics"):
       print("mechanical engineering\n")
elif(sub1=="programming")and(sub2=="maths")or(sub1=="maths" and sub2=="programming"):
       print("computer engineering\n")
elif(sub1=="chemistry")and(sub2=="biology")or(sub1=="biology" and sub2=="chemistry"):
       print("Biotecnology engineering\n")              
elif(sub1=="circuits")and(sub2=="maths")or(sub1=="maths" and sub2=="circuits"):
       print("electronics engineering\n")
elif(sub1=="programming")and(sub2=="statistics")or(sub1=="statistics" and sub2=="programming"):
       print("Artificial inteligence and data science\n")
elif(sub1=="programming")and(sub2=="AI concepts")or(sub1=="AI concept" and sub2=="programming"):
       print("artificial inteligence and machine learning engineering\n")              
