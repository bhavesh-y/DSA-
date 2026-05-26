def find_paper(papers,name):
    for paper in papers:
        if paper == name:
            return True
        
        return False


papers = ["Anita","Bharat","Sahil","ayush" , "Bhavna", "chirag", "divya","Emran","Om","Sneha","Udit","raghav" ]

search_name = "karan"

result = find_paper(papers, search_name)

if result:
    print("paper found")

else:
    print("Not found")