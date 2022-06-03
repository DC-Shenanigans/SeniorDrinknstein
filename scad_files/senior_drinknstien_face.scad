include <display_mount.scad>;
include <button_cutout.scad>;
include <senior_drinknstien_body.scad>;

body_width = 230;
body_depth = 150;
body_height = 230;  
shell_thickness = 4;
//linear_extrude(2) polygon(points=[0,0,0][50,50,50]);
module face(){

    difference(){
        cube([body_width,body_depth,body_height]);
        translate([body_width/ 2 - 50,10,body_height - 70]) #display_mount();
        translate([22,-2,body_height - 100]) button_cutout();
        translate([22,-2,body_height - 140]) button_cutout();
        translate([22,-2,body_height - 180]) button_cutout();
        translate([22,-2,body_height - 220]) button_cutout();
        translate([body_width - 40,-2,body_height - 100]) button_cutout();
        translate([body_width - 40,-2,body_height - 140]) button_cutout();
        translate([body_width - 40,-2,body_height - 180]) button_cutout();
        translate([body_width - 40,-2,body_height - 220]) button_cutout();

        translate([shell_thickness,shell_thickness,0 + shell_thickness]) #cube([body_width - 2 * shell_thickness,body_depth - 2 * shell_thickness + 10,body_height - 2 * shell_thickness]);
        translate([shell_thickness -2,body_depth - 4,-2 + shell_thickness]) #cube([body_width - 2 * shell_thickness + 4,2 * shell_thickness,body_height - 2 * shell_thickness +4]);
        //translate([shell_thickness - 5,shell_thickness,-10]) #cube([body_width - 2 * shell_thickness + 10,body_depth - 2 * shell_thickness + 10,body_height - 2 * shell_thickness - 10]);
    }
}

face();
//translate([shell_thickness - 2,body_depth + 10, shell_thickness - 2]) body();;
