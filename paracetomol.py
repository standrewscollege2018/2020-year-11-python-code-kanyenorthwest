AGE_BOUNDARY = 12
ADULT_DOSAGE = 500
MILLIGRAMS_PER_KG = 10

# asks for age and weight of patient
age = int(input("What is the patient's age? "))
weight = int(input("What is the patient's weight? "))

# if the patient is 12 or over it is 500 mg paracetamol tablets
if age >= AGE_BOUNDARY:
    print("Take 2x doses of {}mg paracetamol tablets.".format(ADULT_DOSAGE))
elif age < AGE_BOUNDARY:
    dosage = MILLIGRAMS_PER_KG * weight
    print("Recommended dosage is {}mg paracetamol tablets.".format(MILLIGRAMS_PER_KG * weight))
    
    
    
    
    #ryan stewart has a pet mouse