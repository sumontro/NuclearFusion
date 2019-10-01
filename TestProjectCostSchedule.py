# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:46:57 2019

@author: sumontro.sinha
"""

#class ProjectCostSchedule():
# def __init__(self, name=""):
    
  #Design Average Variables
#  self.name = name
number_of_designs = 50
simulation_setup_parameters_avg = 40
coding_speed_avg = 50 #[lines/s]
data_file_size_avg = 1 #[GB/s]
processing_speed_avg = 2.4 #[GB/s]
number_of_engineers_avg = 4
engineer_wage_avg = 30 #[$/hr]
software_cost_avg = 5000 #[$/license]
computer_cost_avg = 2500 #[$/unit]
understanding_time_avg = 2 #[hrs]
  
#Design Standard Deviation Variables
simulation_setup_parameters_stddev = 40
coding_speed_stddev = 50 #[lines/s]
data_file_size_stddev = 1 #[GB/s]
processing_speed_stddev = 2.4 #[GB/s]
number_of_engineers_stddev = 4
engineer_wage_stddev = 30 #[$/hr]
software_cost_stddev = 5000 #[$/license]
computer_cost_stddev = 2500 #[$/unit]   
understanding_time_stddev = 1 #[hrs]
 
#Production Average Variables
number_prototypes = 40
production_setup_mass_avg = 15 #[kg]
mass_carried_per_person_avg = 5 #[kg/person]
speed_of_person_avg = 1 #[m/s]
length_of_travel_setup_avg = 50 #[m]
number_of_people_fabrication_avg = 4 #[people]
production_mass_needed_avg = 1500 #[kg]
production_mass_flow_avg = 0.05 #[kg/s]
finishing_mass_avg = 150 #[kg]
finishing_mass_flow_avg = 0.05 #[kg/s]
assembly_distance_to_travel_avg = 3000 #[m]
number_of_finishing_machines_avg = 10 #[units]
number_of_assemblers_avg = 15 #[people]
number_of_production_machines_avg = 10 #[units]
mass_liftable_by_assemblers_avg = 15 #[kg]
assembly_speed_avg = 1 #[m/s]
assembly_wage_avg = 19 #[$/hr]
production_machine_cost_avg = 300 #[$/unit]
finishing_machine_cost_avg = 5000 #[$/unit]
assembly_machine_cost_avg = 25000 #[$/unit]
material_cost_avg = 15 #[$/kg]
  
#Production Standard Deviation Variables
production_setup_mass_stddev = 4 #[kg]
mass_carried_per_person_stddev = 5 #[kg/person]
speed_of_person_stddev = 1 #[m/s]
length_of_travel_setup_stddev = 50 #[m]
number_of_people_fabrication_stddev = 4 #[people]
production_mass_needed_stddev = 1500 #[kg]
production_mass_flow_stddev = 0.05 #[kg/s]
finishing_mass_stddev = 150 #[kg]
finishing_mass_flow_stddev = 0.05 #[kg/s]
assembly_distance_to_travel_stddev = 3000 #[m]
number_of_finishing_machines_stddev = 10 #[units]
number_of_assemblers_stddev = 15 #[people]
number_of_production_machines_stddev = 10 #[units]
mass_liftable_by_assemblers_stddev = 15 #[kg]
assembly_speed_stddev = 1 #[m/s]
assembly_wage_stddev = 19 #[$/hr]
production_machine_cost_stddev = 300 #[$/unit]
finishing_machine_cost_stddev = 5000 #[$/unit]
assembly_machine_cost_stddev = 25000 #[$/unit]
material_cost_stddev = 15 #[$/kg]
  
    
     
#Testing Average Variables 
number_tests = 15 
test_setup_mass_avg = 1500 #[kg]
test_travel_distance_avg = 50 #[m]
testing_staff_number_avg = 5 #[people]
firing_energy_avg = 100000 #[J]
charging_power_avg = 10000 #[W]
SOP_Number_of_Steps_avg = 15 #[steps]
SOP_clearance_rate_avg = 0.1 #[steps/s]
residual_radioactivity_halflife_avg = 0 #[hrs]
Data_quantitity_gathered_avg = 1 #[TB]
download_speed_avg = 5 #[GB/s]
cleanup_mass_avg = 15 #[kg]
test_wage_avg = 19 #[$/hr]
number_sensors_needed_avg = 150 #[units]
number_sensors_broken_avg = 15 #[units/test]
sensor_cost_avg = 2500 #[$/unit]
power_supply_cost_avg = 3 #[$/W]
test_material_cost_avg = 15 #[$/kg]
testing_staff_wage_avg = 30 #[$/hr]
charging_power_LCOE_cost_avg = 2 #[$/W]

#Testing Standard Deviation Variables 
test_setup_mass_stddev = 1500 #[kg]
test_travel_distance_stddev = 50 #[m]
testing_staff_number_stddev = 5 #[people]
firing_energy_stddev = 100000 #[J]
charging_power_stddev = 10000 #[W]
SOP_Number_of_Steps_stddev = 15 #[steps]
SOP_clearance_rate_stddev = 0.1 #[steps/s]
residual_radioactivity_halflife_stddev = 0 #[hrs]
Data_quantitity_gathered_stddev = 1 #[TB]
download_speed_stddev = 5 #[GB/s]
cleanup_mass_stddev = 15 #[kg]
test_wage_stddev = 19 #[$/hr]
number_sensors_needed_stddev = 150 #[units]
number_sensors_broken_stddev = 15 #[units/test]
sensor_cost_stddev = 2500 #[$/unit]
power_supply_cost_stddev = 3 #[$/W]
test_material_cost_stddev = 15 #[$/kg]
testing_staff_wage_stddev = 10 #[$/hr]
charging_power_LCOE_cost_stddev = 1 #[$/W]
  
total_schedule_check_months = 12 #[months]
total_cost_check_thousands = 550 #[$ thousands]

total_schedule_check = total_schedule_check_months
total_cost_check = total_cost_check_thousands*1000
      
# def calc(self):
schedule_failure_count = 0
schedule_success_count = 0

budget_failure_count = 0
budget_success_count = 0

for i in range(100000): 
    if random.uniform(0,1) < 0.5:
       #Design
       computer_cost = computer_cost_avg + random.uniform(0,1)*computer_cost_stddev
       software_cost = software_cost_avg + random.uniform(0,1)*software_cost_stddev
       engineer_wage = engineer_wage_avg + random.uniform(0,1)*engineer_wage_stddev
       number_of_engineers = number_of_engineers_avg + random.uniform(0,1)*number_of_engineers_stddev
       simulation_setup_parameters = simulation_setup_parameters_avg + random.uniform(0,1)*simulation_setup_parameters_stddev
       coding_speed = coding_speed_avg + random.uniform(0,1)*coding_speed_stddev
       data_file_size = data_file_size_avg + random.uniform(0,1)*data_file_size_stddev
       processing_speed = processing_speed_avg + random.uniform(0,1)*processing_speed_stddev
        
       #Production/Prototyping
       material_cost = material_cost_avg + random.uniform(0,1)*material_cost_stddev
       fabrication_machine_cost = production_machine_cost_avg + random.uniform(0,1)*production_machine_cost_stddev
       finishing_machine_cost = finishing_machine_cost_avg + random.uniform(0,1)*finishing_machine_cost_stddev
       assembly_machine_cost = assembly_machine_cost_avg + random.uniform(0,1)*assembly_machine_cost_stddev
       assembly_wage = assembly_wage_avg + random.uniform(0,1)*assembly_wage_stddev
       production_setup_mass = production_setup_mass_avg + random.uniform(0,1)*production_setup_mass_stddev
       mass_carried_per_person = mass_carried_per_person_avg + random.uniform(0,1)*mass_carried_per_person_stddev
       speed_of_person = speed_of_person_avg + random.uniform(0,1)*speed_of_person_stddev
       length_of_travel_setup = length_of_travel_setup_avg + random.uniform(0,1)*length_of_travel_setup_stddev
       assembly_stafF_number = number_of_people_fabrication_avg + random.uniform(0,1)*number_of_people_fabrication_stddev
       production_mass_needed = production_mass_needed_avg + random.uniform(0,1)*production_mass_needed_stddev
       number_of_production_machines = number_of_production_machines_avg + random.uniform(0,1)*number_of_production_machines_stddev
       production_mass_flow = production_machine_cost_avg + random.uniform(0,1)*production_machine_cost_stddev
       finishing_mass = finishing_mass_avg + random.uniform(0,1)*finishing_mass_stddev
       number_of_finishing_machines = number_of_finishing_machines_avg + random.uniform(0,1)*number_of_finishing_machines_stddev
       finishing_mass_flow = finishing_mass_flow_avg + random.uniform(0,1)*finishing_mass_flow_stddev 
       assembly_distance_travel = assembly_distance_to_travel_avg + random.uniform(0,1)*assembly_distance_to_travel_stddev
       number_of_assemblers = number_of_assemblers_avg + random.uniform(0,1)*number_of_assemblers_stddev 
       mass_liftable_by_assemblers = mass_liftable_by_assemblers_avg + random.uniform(0,1)*mass_liftable_by_assemblers_stddev
       assembly_speed = assembly_speed_avg + random.uniform(0,1)*assembly_speed_stddev
        
       #Testing
       test_setup_mass = test_setup_mass_avg + random.uniform(0,1)*test_setup_mass_stddev
       travel_distance_to_carry_testmass = test_travel_distance_avg + random.uniform(0,1)*test_material_cost_stddev
       testing_staff_number = testing_staff_number_avg + random.uniform(0,1)*testing_staff_number_stddev
       firing_energy = firing_energy_avg + random.uniform(0,1)*firing_energy_stddev
       charging_power = charging_power_avg + random.uniform(0,1)*charging_power_stddev
       SOP_Number_of_steps = SOP_Number_of_Steps_avg + random.uniform(0,1)*SOP_Number_of_Steps_stddev 
       SOP_clearance_rate = SOP_clearance_rate_avg + random.uniform(0,1)*SOP_clearance_rate_stddev
       residual_radioactivity_halflife = residual_radioactivity_halflife_avg + random.uniform(0,1)*residual_radioactivity_halflife_stddev
       Data_quantitity_gathered = Data_quantitity_gathered_avg + random.uniform(0,1)*Data_quantitity_gathered_stddev
       download_speed = download_speed_avg + random.uniform(0,1)*download_speed_stddev
       cleanup_mass = cleanup_mass_avg + random.uniform(0,1)*cleanup_mass_stddev
       understanding_time = understanding_time_avg + random.uniform(0,1)*understanding_time_stddev
       testing_staff_wage = testing_staff_wage_avg + random.uniform(0,1)*testing_staff_wage_stddev
       charging_power_LCOE_cost = charging_power_LCOE_cost_avg + random.uniform(0,1)*charging_power_LCOE_cost_stddev
        
    else:
       #Design
       computer_cost = computer_cost_avg - random.uniform(0,1)*computer_cost_stddev
       software_cost = software_cost_avg - random.uniform(0,1)*software_cost_stddev
       engineer_wage = engineer_wage_avg - random.uniform(0,1)*engineer_wage_stddev
       number_of_engineers = number_of_engineers_avg - random.uniform(0,1)*number_of_engineers_stddev
       simulation_setup_parameters = simulation_setup_parameters_avg - random.uniform(0,1)*simulation_setup_parameters_stddev
       coding_speed = coding_speed_avg - random.uniform(0,1)*coding_speed_stddev
       data_file_size = data_file_size_avg - random.uniform(0,1)*data_file_size_stddev
       processing_speed = processing_speed_avg - random.uniform(0,1)*processing_speed_stddev
        
       #Production/Prototyping
       material_cost = material_cost_avg - random.uniform(0,1)*material_cost_stddev
       fabrication_machine_cost = production_machine_cost_avg - random.uniform(0,1)*production_machine_cost_stddev
       finishing_machine_cost = finishing_machine_cost_avg - random.uniform(0,1)*finishing_machine_cost_stddev
       assembly_machine_cost = assembly_machine_cost_avg - random.uniform(0,1)*assembly_machine_cost_stddev
       assembly_wage = assembly_wage_avg - random.uniform(0,1)*assembly_wage_stddev
       production_setup_mass = production_setup_mass_avg - random.uniform(0,1)*production_setup_mass_stddev
       mass_carried_per_person = mass_carried_per_person_avg - random.uniform(0,1)*mass_carried_per_person_stddev
       speed_of_person = speed_of_person_avg - random.uniform(0,1)*speed_of_person_stddev
       length_of_travel_setup = length_of_travel_setup_avg - random.uniform(0,1)*length_of_travel_setup_stddev
       assembly_staff_number = number_of_people_fabrication_avg - random.uniform(0,1)*number_of_people_fabrication_stddev
       production_mass_needed = production_mass_needed_avg - random.uniform(0,1)*production_mass_needed_stddev
       number_of_production_machines = number_of_production_machines_avg - random.uniform(0,1)*number_of_production_machines_stddev
       production_mass_flow = production_machine_cost_avg - random.uniform(0,1)*production_machine_cost_stddev
       finishing_mass = finishing_mass_avg - random.uniform(0,1)*finishing_mass_stddev
       number_of_finishing_machines = number_of_finishing_machines_avg - random.uniform(0,1)*number_of_finishing_machines_stddev
       finishing_mass_flow = finishing_mass_flow_avg - random.uniform(0,1)*finishing_mass_flow_stddev 
       assembly_distance_travel = assembly_distance_to_travel_avg - random.uniform(0,1)*assembly_distance_to_travel_stddev
       number_of_assemblers = number_of_assemblers_avg - random.uniform(0,1)*number_of_assemblers_stddev 
       mass_liftable_by_assemblers = mass_liftable_by_assemblers_avg - random.uniform(0,1)*mass_liftable_by_assemblers_stddev
       assembly_speed = assembly_speed_avg - random.uniform(0,1)*assembly_speed_stddev
        
       #Testing
       test_setup_mass = test_setup_mass_avg - random.uniform(0,1)*test_setup_mass_stddev
       travel_distance_to_carry_testmass = test_travel_distance_avg - random.uniform(0,1)*test_material_cost_stddev
       testing_staff_number = testing_staff_number_avg - random.uniform(0,1)*testing_staff_number_stddev
       firing_energy = firing_energy_avg - random.uniform(0,1)*firing_energy_stddev
       charging_power = charging_power_avg - random.uniform(0,1)*charging_power_stddev
       SOP_Number_of_steps = SOP_Number_of_Steps_avg - random.uniform(0,1)*SOP_Number_of_Steps_stddev 
       SOP_clearance_rate = SOP_clearance_rate_avg - random.uniform(0,1)*SOP_clearance_rate_stddev
       residual_radioactivity_halflife = residual_radioactivity_halflife_avg - random.uniform(0,1)*residual_radioactivity_halflife_stddev
       Data_quantitity_gathered = Data_quantitity_gathered_avg - random.uniform(0,1)*Data_quantitity_gathered_stddev
       download_speed = download_speed_avg - random.uniform(0,1)*download_speed_stddev
       cleanup_mass = cleanup_mass_avg - random.uniform(0,1)*cleanup_mass_stddev
       understanding_time = understanding_time_avg - random.uniform(0,1)*understanding_time_stddev
       testing_staff_wage = testing_staff_wage_avg - random.uniform(0,1)*testing_staff_wage_stddev
       charging_power_LCOE_cost = charging_power_LCOE_cost_avg + random.uniform(0,1)*charging_power_LCOE_cost_stddev
      
       #Design Components 
       setup_time_design = (simulation_setup_parameters/(coding_speed*number_of_engineers))/3600 #[hrs]
       processing_time_design = (data_file_size*production_mass_needed/(processing_speed*number_of_engineers))/3600 #[hrs}
       post_processing_time_design = processing_time_design 
       total_design_time = number_of_designs*(understanding_time + setup_time_design + processing_time_design + post_processing_time_design) 
       total_design_cost = number_of_engineers*(computer_cost + software_cost + engineer_wage*total_design_time)
      
       #Production Components 
       production_setup_speed = mass_carried_per_person*speed_of_person*number_of_assemblers/assembly_distance_travel
       setup_time_production = (production_setup_mass/production_setup_speed)/3600 
       production_time = (production_mass_needed/(number_of_production_machines*production_mass_flow))/3600
       finishing_time_production = (finishing_mass/(finishing_mass_flow*number_of_finishing_machines))/3600
       assembly_time_production = (production_mass_needed/(mass_liftable_by_assemblers*speed_of_person*number_of_assemblers/assembly_distance_travel))/3600
       total_production_time = number_prototypes*(setup_time_production + production_time + finishing_time_production + assembly_time_production) 
       total_production_cost = fabrication_machine_cost*number_of_production_machines + finishing_machine_cost*number_of_finishing_machines + assembly_machine_cost*number_of_assemblers + assembly_staff_number*total_production_time*assembly_wage + material_cost*(production_setup_mass + production_mass_needed + finishing_mass) 
      
       #Testing Components
       test_setup_massflow = mass_carried_per_person/(testing_staff_number*travel_distance_to_carry_testmass*speed_of_person) + mass_liftable_by_assemblers/(number_of_assemblers*travel_distance_to_carry_testmass*speed_of_person)
       setup_time_testing = (test_setup_mass/test_setup_massflow)/3600
       firing_time_testing = ((firing_energy/charging_power)/3600)+(SOP_Number_of_steps/SOP_clearance_rate)/3600
       processing_time_testing = ((Data_quantitity_gathered*1000/download_speed)+(Data_quantitity_gathered*1000/processing_speed))/3600
       cleanup_time_testing = (cleanup_mass/test_setup_massflow)/3600
       repair_time_testing = total_production_time*cleanup_mass/production_mass_needed
       total_testing_time = number_tests*(setup_time_testing + firing_time_testing + processing_time_testing + cleanup_time_testing + repair_time_testing)
       charging_power_cost = charging_power_LCOE_cost*charging_power
       total_testing_cost = number_tests*total_production_cost*(cleanup_mass/production_mass_needed) + number_tests*total_testing_time*testing_staff_number*testing_staff_wage + charging_power_cost + material_cost*(test_setup_mass) + number_of_assemblers*assembly_machine_cost
    
    total_schedule = (total_design_time + total_production_time + total_testing_time)/(24*30) 
    total_cost = total_design_cost + total_production_cost + total_testing_cost 
    

    
    if total_schedule <= total_schedule_check:
      schedule_success_count = schedule_success_count + 1
#      print(schedule_success_count)
    else:
      schedule_failure_count = schedule_failure_count + 1 
#      print(schedule_failure_count)
    if total_cost <= total_cost_check:
      budget_success_count = budget_success_count + 1
#      print(budget_success_count)
    else:
      budget_failure_count = budget_failure_count + 1
#      print(budget_failure_count)
    
schedule_success_fraction = (schedule_success_count/100000)*100
budget_success_fraction = (budget_success_count/100000)*100
 
#print("computer cost %f " % (computer_cost))
#print("total testing time %f hrs" % (total_testing_time))
#print("total production time %f hrs" % (total_production_time))
#print("total design time %f hrs" % (total_design_time))
#print("total schedule %f months" % (total_schedule))
print("schedule success %f percent" % (schedule_success_fraction))
print("budget success %f percent" % (budget_success_fraction))
print("schedule %f months" % (total_schedule_check))
print("budget $%f" % (total_cost_check))
#    
#def FluxCompressor(x,name=""):
#FluxCompressor = ProjectCostSchedule(name)
#x = range(5)
#FluxCompressor.total_schedule_check_months = 12 + 8*x
#FluxCompressor.total_cost_check_thousands = 100 + 50*x
#FluxCompressor.calc()
#FluxCompressor.printinfo()
#return FluxCompressor 

#print(FluxCompressor.calc)


#    