

# def calculate_energy_expended(activity_type, duration_minutes, intensity)calculate_energy_expended
def calculate_energy_expended(activity_type, duration_minutes, intensity):
    if activity_type== "running":
        if intensity=="low":
            intensity=10
        elif intensity=="medium":
            intensity=14
        elif intensity=="high":
            intensity=18
    elif activity_type=="cycling":
        if intensity=="low":
            intensity=7
        elif intensity== "medium":
            intensity=11
        elif intensity=="high":
            intensity=15
    elif activity_type=="swimming":
        if intensity=="low":
            intensity=9
        elif intensity=="medium":
            intensity=13
        elif intensity=="high":
            intensity=17
    total_energy=intensity*duration_minutes
# Return the total energy expended                    
    return total_energy

def calculate_performance_intensity(age, baseline_hr, training_hr):
    max_heart_rate= 220 - age
    heart_rate_reserve=max_heart_rate - baseline_hr
    intensity_percentage= (training_hr - baseline_hr) / heart_rate_reserve * 100
    return round(intensity_percentage,1)

def determine_effort_level(intensity_percentage):
    if intensity_percentage<50:
        return 'Recovery Level'
    elif intensity_percentage<60:
        return 'Endurance Level'
    elif intensity_percentage<70:
        return "Aerobic Level"
    elif intensity_percentage<85:
        return "Threshold Level"
    else:
        return "Peak Power Level"

def  calculate_training_points(energy, duration, level_bonus):
    base_point= energy*0.1+ duration*2
    if level_bonus == "Recovery":  
        level_bonus=0.5
    elif level_bonus=="Endurance":
        level_bonus= 1.0
    elif level_bonus=="Aerobic":
        level_bonus=1.2
    elif level_bonus=="Threshold":
        level_bonus= 1.5
    elif level_bonus=="Peak":
        level_bonus=1.8
    else:
        return "Error"
    final_points= base_point * level_bonus
    return  final_points 

def requires_recovery(training_days, total_minutes, avg_intensity):
    
    if training_days>=6:
         return True
    elif total_minutes>450 and avg_intensity>70:
        return True
    elif training_days>=4 and avg_intensity>80:
        return True
    else:
        return False
def generate_training_summary(athlete, activity_type, duration, intensity, age, baseline_hr, training_hr, training_days):
    total_energy =  calculate_energy_expended(activity_type, duration, intensity)
    intensity_percent = calculate_performance_intensity(age, baseline_hr, training_hr)
    level_bonus = determine_effort_level(intensity_percent)
    final_points=calculate_training_points(total_energy, duration, level_bonus)
    recovery=requires_recovery(training_days, duration, intensity_percent)   
    print("SPORTS TRAINING ANALYZER")
    print(f"="*40)
    print(f'Training Summary for: {athlete} ')
    print(f"-"*40)
    print(f'Activity type:{activity_type}')
    print(f"Duration:{duration} minutes")
    print(f"Intensity Level:{intensity}")
    print(f"Energy Expended:{total_energy}")
    print("Performance Analysis: ")
    print(f'  Age:{age} , Baseline hr:{baseline_hr}, Training hr:{training_hr}')
    print( f' Intensity:{intensity_percent:.1f} %')
    print(f"  Effort Level:{level_bonus}")
    print(f"Training Points:{final_points}")
    print(f'Consecutive Training Days:{training_days}')
    print(f'Recovery Day Required:{recovery}')


# Define a function generate_training_summary(athlete, activity_type, duration, intensity, age, baseline_hr, training_hr, training_days) that:
# Calls all necessary functions to calculate metrics
# Prints a formatted summary (no return value)
# Include all calculated values and recommendations
# Testing Inputs: Test your system with these training sessions:
     
# Session 1: “Sam”, “running”, 45 minutes, “high”, age=28, baseline_hr=65, training_hr=155, training_days=3
generate_training_summary('Sam','running', 45, 'high',28 , 65, 155 , 3 )
# Session 2: “Morgan”, “cycling”, 60 minutes, “medium”, age=35, baseline_hr=70, training_hr=140, training_days=5
generate_training_summary('Morgan', "cycling" , 60, "medium",35,  70, 140,5)
# Session 3: “Taylor”, “swimming”, 30 minutes, “low”, age=42, baseline_hr=68, training_hr=95, training_days=7

generate_training_summary('Taylor', 'swimming',30, 'low',42,68,95,7)
