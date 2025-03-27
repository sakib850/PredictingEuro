from scipy.stats import poisson
lamb_home = 1.4 * 0.8
lamb_away  = 1.2 * 0.9
prob_away , prob_draw ,prob_home=0,0,0
for x in range (0,11): #number of goals for home team 
            for y in range (0,11):# number of goals for away team
                p = poisson.pmf(x, lamb_home) * poisson.pmf(y, lamb_away)
                if x==y:
                    prob_draw +=p
                elif x > y :
                    prob_home += p
                elif x < y :
                    prob_away += p
                    
points_home = 3* prob_home + prob_draw
points_away = 3* prob_away + prob_draw


print(points_home,points_away)

