# weird sum thing idk


#function for present discount value
def present_discount_value(face_value, interest_rate_spread, discount_rate, maturity):

    SumThing = 0
    for index in range(1,maturity+1): #only accepts whole integer values!
        SumThing += (1 + discount_rate)**(-index)

    return SumThing * face_value * interest_rate_spread


print(present_discount_value(500, 0.01, 0.03, 5))

#function for the other thing
def other_thing(value, interest_rate, maturity):

    SumThing = 0
    for index in range(1,maturity+1): #only accepts whole integer values!
        SumThing += (1 + interest_rate)**(-index)

    return SumThing * value #this is the stupid simple case where stuff is constant



