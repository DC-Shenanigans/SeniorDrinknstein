
module button_cutout(){
    button_radius = 8;

    translate([button_radius,0,button_radius]) rotate([270,0,0])  cylinder(40,button_radius,    button_radius);
}
