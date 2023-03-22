def years_of_growth(initial_population, target_population, growth_rate, net_migration):
        def grow(s, g, nm):
                return s + (s*g) + nm
        current_pop = initial_population
        years = 0
        grow_factor = growth_rate / 100
        while current_pop <= target_population :
                current_pop = grow(current_pop, grow_factor, net_migration)
                years += 1
                print(current_pop)

        return years

        

print(years_of_growth(10000, 7100, 2, 12))

