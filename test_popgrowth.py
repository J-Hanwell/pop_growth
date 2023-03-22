from popgrowtth import years_of_growth

def test_returns_a_number():
    result = years_of_growth(1, 2, 3, 4)
    assert type(result) == float 
