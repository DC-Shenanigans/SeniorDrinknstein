include <pump_mount.scad>;

body_width = 230;
body_depth = 100;
body_height = 230;

module body(){
    shell_thickness = 4;

    difference(){
        cube([body_width,body_depth,body_height]);
        translate([shell_thickness,shell_thickness,shell_thickness])
            #cube([body_width - shell_thickness * 2,body_depth - shell_thickness * 2 + 20, 10 + body_height - shell_thickness * 2]);
        inset = (body_width - ((body_width / 5) * 4) )/ 2;
        translate([inset,-10,10])
            #cube([(body_width / 5) * 4, 20, 20]);
        //translate([body_width/2,0,body_height/2]) rotate([90,0,0]) #cylinder(r=40, h=10, center=true);
        // Add our pump mounts
        rotate([0,0,0]) translate([0,0,body_height - 25])  pump_mount();
        rotate([0,0,0]) translate([body_width - 70,0,body_height - 25])  pump_mount();
        rotate([0,0,0]) translate([body_width / 3 + 7,0,body_height - 25])  pump_mount();
        rotate([0,0,0]) translate([35,0,body_height - 70])  pump_mount();
        rotate([0,0,0]) translate([125,0,body_height - 70])  pump_mount();

        rotate([0,0,0]) translate([0,0,body_height - 115])  pump_mount();
        rotate([0,0,0]) translate([body_width - 70,0,body_height - 115])  pump_mount();
        rotate([0,0,0]) translate([body_width / 3 + 7,0,body_height - 115])  pump_mount();
        rotate([0,0,0]) translate([35,0,body_height - 160])  pump_mount();
        //rotate([0,0,0]) translate([125,0,body_height - 175])  pump_mount();
        //translate([body_width/24,0,body_height - 30]) rotate([0,0,0]) pump_mount();
       
    }
}



body();
