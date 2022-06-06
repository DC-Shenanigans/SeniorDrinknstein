include <display_mount.scad>;

display_housing_width = 152;
display_housing_depth = 30;
display_housing_height = 80;

shell_thickness = 2;


//translate up 60 the pcb height to normalize to 0

difference(){
    cube([display_housing_width,display_housing_depth,display_housing_height]);
    translate([shell_thickness, 0, shell_thickness]) #cube([display_housing_width - shell_thickness * 2,display_housing_depth - shell_thickness * 2,display_housing_height - shell_thickness * 2]);
    translate([27.85 ,display_housing_depth - shell_thickness - 5,60 + 9]) rotate([180,0,0]) #display_mount();
    translate([display_housing_width -8, 0 ,display_housing_height- 8]){
        #cube([8,display_housing_depth,8]);
    }

}