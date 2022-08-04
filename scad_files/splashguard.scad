shell_thickness = 1;

plexiglass_thickness = 2.5;

side_bar_length = 100;
side_bar_width = plexiglass_thickness + shell_thickness * 2;
side_bar_height = 15;

plexiglass_length = side_bar_length - shell_thickness * 2;
plexiglass_height = 220;
module plexi_mount(){
 difference(){
translate([5,-10,0]) cube([side_bar_length - 10, 20,5]);
    translate([shell_thickness,shell_thickness,shell_thickness])
    #cube([plexiglass_length,plexiglass_thickness,plexiglass_height]);
}

difference(){
    cube([side_bar_length,side_bar_width,side_bar_height]);
    translate([shell_thickness,shell_thickness,shell_thickness])
    #cube([plexiglass_length,plexiglass_thickness,plexiglass_height]);
}
}

//translate([0,-5,0]) 
plexi_mount();

//rotate([0,0,135]) translate([0,0,0]) plexi_mount();
//rotate([0,0,90]) translate([70,70,0]) plexi_mount();