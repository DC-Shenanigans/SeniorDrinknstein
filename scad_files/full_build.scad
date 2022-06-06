include <buck_converter.scad>;
include <pi_mount.scad>;
include <relay_mount.scad>;
include <power_board.scad>;
include <alt_power_distribution_board.scad>;


pi_board_y = 54;
pi_board_x = 40;

relay_board_x = 13.25;
relay_board_y = 66.25;
power_board_x = 19.3;
power_board_y = 99;
buck_converter_x = 43;
buck_converter_y = 21;

$fn=20;

module all_the_parts(shell_thickness=1){
        

    translate([10 ,relay_board_y + 15 ,0]) pi_mount(shell_thickness);

    relay(shell_thickness);
    translate([relay_board_x + 5,0,0])  relay(shell_thickness);
    translate([(relay_board_x + 5) * 2,0,0])  relay(shell_thickness);
    translate([(relay_board_x + 5) * 3,0,0])  relay(shell_thickness);
    translate([(relay_board_x + 5) * 4,0,0])  relay(shell_thickness);
    translate([(relay_board_x + 5) * 5,0,0])  relay(shell_thickness);
    //translate([(relay_board_x + 5) * 6,0,0])  relay();


    translate([0,relay_board_y + 30 + pi_board_x]){
        
        translate([0,2,0]) relay(shell_thickness);
        translate([relay_board_x + 5,2,0])  relay(shell_thickness);
        translate([(relay_board_x + 5) * 2,2,0])  relay(shell_thickness);
        translate([(relay_board_x + 5) * 3,2,0])  relay(shell_thickness);
        translate([(relay_board_x + 5) * 4,2,0])  relay(shell_thickness);
        translate([(relay_board_x + 5) * 5,2,0])  relay(shell_thickness);
    //translate([(relay_board_x + 5) * 6,0,0])  relay();
    }

    translate([(relay_board_x + 3) * 7,0,0]) power_distribution_board(shell_thickness);

    translate([(relay_board_x + 3) * 7,45 + power_board_y,0]) power_distribution_board(shell_thickness);


    translate( [relay_board_y + 15,buck_converter_y + relay_board_y + 15,0]) rotate([0,0,270]) buck_converter(shell_thickness);

    translate( [relay_board_y + 15,buck_converter_y + relay_board_y + 10 + buck_converter_y + 10,0]) rotate([0,0,270]) buck_converter(shell_thickness);
}
shell_thickness = 3;
difference(){
    cube([148,210,shell_thickness]);
    translate([shell_thickness,shell_thickness,0]) #cube([142,204,shell_thickness]);
}

translate([0,79,0]) difference(){
     {
        cube([148,50,shell_thickness]);
        translate([shell_thickness * 2,shell_thickness * 2 - 2,0]) #cube([138,42,shell_thickness]);
        
    }
    
}
translate([0,64,0]) difference(){
     {
        cube([148,82,shell_thickness]);
        translate([shell_thickness * 2,shell_thickness * 2,0]) #cube([138,70,shell_thickness]);
        
    }
    
}

all_the_parts(shell_thickness);

