include <display_mount.scad>;
include <button_cutout.scad>;
include <senior_drinknstien_body.scad>;
include <pi_mount.scad>;
include<relay_mount.scad>;
include<buck_converter.scad>;

$fn=20;

body_width = 230;
body_depth = 85;
body_height = 230;  
shell_thickness = 2.5;
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
        
        for( i = [1 : 13]){
            translate([5 + 15 * i ,10,4]) #cube([10, 60, 250]);
        }

        slit_width=290;
        slit_height=10;
        slit_length=60;
        slit_offset=10;
        
        
        translate([-30,slit_offset,shell_thickness + 10]) #cube([slit_width, slit_length, slit_height]);
        translate([-30,slit_offset,shell_thickness + 30]) #cube([slit_width, slit_length, slit_height]);

        translate([-30,slit_offset,shell_thickness + 50]) #cube([slit_width, slit_length, slit_height]);
        translate([-30,slit_offset,shell_thickness + 70]) #cube([slit_width, slit_length, slit_height]);
        translate([-30,slit_offset,shell_thickness + 90]) #cube([slit_width, slit_length, slit_height]);
        translate([-30,slit_offset,shell_thickness + 110]) #cube([slit_width, slit_length, slit_height]);
        translate([-30,slit_offset,shell_thickness + 130]) #cube([slit_width, slit_length, slit_height]);
        translate([-30,slit_offset,shell_thickness + 150]) #cube([slit_width, slit_length, slit_height]);
        translate([-30,slit_offset,shell_thickness + 170]) #cube([slit_width, slit_length, slit_height]);

        translate([-30,slit_offset,shell_thickness + 190]) #cube([slit_width, slit_length, slit_height]);
        translate([-30,slit_offset,shell_thickness + 210]) #cube([slit_width, slit_length, slit_height]);


        
        translate([shell_thickness,shell_thickness,0 + shell_thickness]) #cube([body_width - 2 * shell_thickness,body_depth - 2 * shell_thickness + 10,body_height - 2 * shell_thickness]);
        translate([shell_thickness -2,body_depth - 4,-2 + shell_thickness]) #cube([body_width - 2 * shell_thickness + 4,2 * shell_thickness,body_height - 2 * shell_thickness +4]);
        //translate([shell_thickness - 5,shell_thickness,-10]) #cube([body_width - 2 * shell_thickness + 10,body_depth - 2 * shell_thickness + 10,body_height - 2 * shell_thickness - 10]);
    }
}

face();
translate([body_width / 2 + 22,shell_thickness,59 + body_height / 3 + 23 ]) rotate([90,90,180]) pi_mount(shell_thickness);

translate([220,shell_thickness,150]) rotate([90,0,180]) relay();
translate([190,shell_thickness,150]) rotate([90,0,180]) relay();
translate([55,shell_thickness,150]) rotate([90,0,180]) relay();
translate([25,shell_thickness,150]) rotate([90,0,180]) relay();

translate([187,shell_thickness,90]) rotate([90,90,180]) relay();
translate([112,shell_thickness,90]) rotate([90,90,180]) relay();
translate([187,shell_thickness,70]) rotate([90,90,180]) relay();
translate([112,shell_thickness,70]) rotate([90,90,180]) relay();
translate([187,shell_thickness,50]) rotate([90,90,180]) relay();
translate([112,shell_thickness,50]) rotate([90,90,180]) relay();
translate([187,shell_thickness,30]) rotate([90,90,180]) relay();
translate([112,shell_thickness,30]) rotate([90,90,180]) relay();

translate([171,shell_thickness,100]) rotate([90,0,180]) buck_converter();
translate([80,shell_thickness,100]) rotate([90,0,180]) buck_converter();


//translate([ body_height / 4 + 2 ,shell_thickness,18.25 + 100]) rotate([90,0,180]) relay();

//translate([body_height / 3 + 30,shell_thickness,18.25 + 80]) rotate([90,90,180]) relay();
//translate([shell_thickness - 2,body_depth + 10, shell_thickness - 2]) body();;
