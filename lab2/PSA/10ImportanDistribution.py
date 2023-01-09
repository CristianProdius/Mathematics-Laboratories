import random

couth_controlor_probability = 0.05
must_pay_probability = 0.02

the_rebel_one_for_1_year = 0
count_cought_by_contolor = 0
encounter_hairy_taxator = 0

the_normal_ones_pay_for_1_year = 6*700
for _ in range(700):
    if random.choices(["good lady", "hary muscular ciuvac"], [1-must_pay_probability, must_pay_probability]) == ["hary muscular ciuvac"]:
        the_rebel_one_for_1_year += 6
        encounter_hairy_taxator += 1
    else:
        if random.choices(["free to ride", "cought"], [1-couth_controlor_probability, couth_controlor_probability]) == ["cought"]:
            count_cought_by_contolor += 1
            if count_cought_by_contolor == 1:
                the_rebel_one_for_1_year += 50
            elif count_cought_by_contolor == 2:
                the_rebel_one_for_1_year += 150
            else:
                the_rebel_one_for_1_year += 300

print("The rebel encounter a hairy taxator: ", encounter_hairy_taxator)
print("The rebel student was cought by the contolor:", count_cought_by_contolor)
print("Total sub that the rebel spended was: ", the_rebel_one_for_1_year)
print("*******************************")
print("Conclusion: ")
print("the normal ones pay: ", the_normal_ones_pay_for_1_year, "which is with: ", the_rebel_one_for_1_year-the_normal_ones_pay_for_1_year, "less the the rebel one")