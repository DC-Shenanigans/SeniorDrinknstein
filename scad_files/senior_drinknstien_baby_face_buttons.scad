include <button_cutout.scad>;

display_housing_width = 151;
display_housing_depth = 30;
display_housing_height = 80;

shell_thickness = 2;


//translate up 60 the pcb height to normalize to 0

difference(){
    cube([display_housing_width,display_housing_depth,display_housing_height]);
    translate([shell_thickness, 0, shell_thickness]) #cube([display_housing_width - shell_thickness * 2,display_housing_depth - shell_thickness * 2,display_housing_height - shell_thickness * 2]);
    
    
    translate([0, 0 ,display_housing_height- 8]){
        #cube([8,display_housing_depth,8]);
    }
    
    translate([15,0,15]) #button_cutout();
    translate([15,0,45]) #button_cutout();
    translate([50,0,15]) #button_cutout();
    translate([50,0,45]) #button_cutout();
    translate([85,0,15]) #button_cutout();
    translate([85,0,45]) #button_cutout();
    translate([120,0,15]) #button_cutout();
    translate([120,0,45]) #button_cutout();
}