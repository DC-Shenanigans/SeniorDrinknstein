
$fs=0.2;
$fn=250;

shell_thickness = 1;
standoff_height = 7;
standoff_bevel_ratio = .75;
standoff_radius = 1.45;

standoff_radius_bevel = standoff_radius * standoff_bevel_ratio;

pin_hole_separation_y = 13.5;
pin_hole_separation_x = 66;

base_width_x = pin_hole_separation_x + 5;
base_depth_y = pin_hole_separation_y + 5;

standoff_start_x = (base_width_x - pin_hole_separation_x) / 2;
standoff_start_y = (base_depth_y - pin_hole_separation_y) / 2;



difference() 
{
    cube([base_width_x, base_depth_y, shell_thickness]);

    translate([standoff_start_x * 2,standoff_start_y * 1.5,-1]) 
    #cube([base_width_x - 10 , base_depth_y- 7.5,   shell_thickness + 3]);
}

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
