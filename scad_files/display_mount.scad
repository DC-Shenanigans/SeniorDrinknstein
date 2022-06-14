

module display_mount(){
    screen_pcb_width = 98.30;
    // adding .1 for tolerances
    screen_cutout_width = 97.10; 
    screen_pcb_height = 60;
    screen_cutout_height = 40.10; //adding .1 for tolerances

    screen_cutout_depth = 12.15;

    screen_cutout_offset = 10;

    screw_hole_radius = 1.75;
    screw_hole_inset = 2.0 ;
    screw_hole_height = 20;


    module screw_hole(){
        rotate([90,0,0]) cylinder(screw_hole_height,screw_hole_radius, screw_hole_radius);
    }
    
    translate([0,-screen_cutout_depth,screen_cutout_offset]) cube([screen_cutout_width,screen_cutout_depth,screen_cutout_height]);

    cube([screen_pcb_width,1,screen_pcb_height]);

    //translate([screw_hole_inset, 5, screw_hole_inset]) screw_hole();
    
    //translate([screw_hole_inset, 5, screen_pcb_height - screw_hole_inset]) screw_hole();
    
    //translate([screen_pcb_width - screw_hole_inset - .7, 5, screen_pcb_height - screw_hole_inset]) screw_hole();
    
    //translate([screen_pcb_width - screw_hole_inset - .7, 5, screw_hole_inset]) screw_hole();
}

//display_mount();
