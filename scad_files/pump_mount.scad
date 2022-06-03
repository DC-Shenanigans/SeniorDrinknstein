
module pump_mount (){
    // Pump mount for Log
    pump_hole_separation = 50;
    pump_hole_inset = 10;

    pump_housing_length = 50 + pump_hole_inset + 10;
    pump_housing_width = 10;

    pump_screw_radius = 1.7;
    pump_hole_center = 0;
    
   
    cylinder_height = pump_housing_width * 1.5;
    cylinder_depth = pump_housing_width*1.1;
    translate([pump_hole_separation + pump_hole_inset,pump_housing_width * 1.1,pump_hole_center])
        rotate([90,0,0])
        cylinder(cylinder_height, pump_screw_radius, pump_screw_radius);
    translate([pump_hole_inset,cylinder_depth,pump_hole_center])
        rotate([90,0,0])
        cylinder(cylinder_height, pump_screw_radius, pump_screw_radius);
    translate([pump_housing_length/2, pump_housing_width*1.1,pump_hole_center])
        rotate([90,0,0])
        cylinder(cylinder_height, 16, 16);
    
}

//pump_mount();