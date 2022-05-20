
$fs=0.2;
$fn=250;

shell_thickness = 2;
standoff_height = 6;
standoff_bevel_ratio = .85;
standoff_radius = 1.35;

standoff_radius_bevel = standoff_radius * standoff_bevel_ratio;

pin_hole_separation_y = 13;
pin_hole_separation_x = 65;

base_width_x = pin_hole_separation_x + 10;
base_depth_y = pin_hole_separation_y + 10;

standoff_start_x = (base_width_x - pin_hole_separation_x) / 2;
standoff_start_y = (base_depth_y - pin_hole_separation_y) / 2;


cube([base_width_x, base_depth_y, shell_thickness]);


// Make the first pin
translate([standoff_start_x,standoff_start_y,0]) 
                            cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
                            
// Make the second pin

translate([standoff_start_x + pin_hole_separation_x,standoff_start_y,0]) 
                            cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
// Make the third pin

translate([standoff_start_x ,standoff_start_y+ pin_hole_separation_y,0]) 
                            cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
                            
// Make the fourth pin

translate([standoff_start_x + pin_hole_separation_x ,standoff_start_y+ pin_hole_separation_y,0]) 
                            cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
