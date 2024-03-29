
module pi_mount(shell_thickness = 1)
{
    //shell_thickness = 1;
    //standoff_height = 6;
    standoff_bevel_ratio = .75;
    standoff_radius = 1.10;
    
    safety_standoff_height = 10;
    safety_standoff_radius = 2.8;

    standoff_height = 4 + safety_standoff_height;

    standoff_radius_bevel = standoff_radius * standoff_bevel_ratio;

    pin_hole_separation_y = 39.75;
    pin_hole_separation_x = 54;

    base_width_x = pin_hole_separation_x + 5;
    base_depth_y = pin_hole_separation_y + 5;

    standoff_start_x = (base_width_x - pin_hole_separation_x) / 2;
    standoff_start_y = (base_depth_y - pin_hole_separation_y) / 2;

    cutout_start_x = (standoff_start_x + 2);
    cutout_start_y = (standoff_start_y  + 1);

    cutout_width_x = (base_width_x - cutout_start_x * 2);
    cutout_depth_y = (base_depth_y - cutout_start_y * 2);
    
    difference() 
    {
        cube([base_width_x , base_depth_y, shell_thickness]);

        translate([cutout_start_x,cutout_start_y,-1]) 
        #cube([cutout_width_x, cutout_depth_y,   shell_thickness + 3]);
    }

    // Make the first pin
    translate([standoff_start_x,standoff_start_y,shell_thickness]) {
            difference(){
                cylinder(safety_standoff_height,safety_standoff_radius,safety_standoff_radius);
                #cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
            }
        }
    
                                
    // Make the second pin

    translate([standoff_start_x + pin_hole_separation_x,standoff_start_y,shell_thickness]) {
            difference(){
                cylinder(safety_standoff_height,safety_standoff_radius,safety_standoff_radius);
                #cylinder(standoff_height,standoff_radius,standoff_radius_bevel);

            }

        }
        
    // Make the third pin

    translate([standoff_start_x ,standoff_start_y+ pin_hole_separation_y,shell_thickness]) {
        difference(){
            cylinder(safety_standoff_height,safety_standoff_radius,safety_standoff_radius);
            #cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
        }
    }
                                
    // Make the fourth pin

    translate([standoff_start_x + pin_hole_separation_x ,standoff_start_y+ pin_hole_separation_y,shell_thickness]) {
        difference(){
            cylinder(safety_standoff_height,safety_standoff_radius,safety_standoff_radius);        
            #cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
        }

        }

}

//pi_mount();