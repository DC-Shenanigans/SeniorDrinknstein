plexiglass_thickness = 2.5;
shell_thickness = 1;
hose_radius = 1.5;
radius_fuzz = 0.5;
fuzzy_radius = hose_radius + radius_fuzz;
$fn = 150;


pour_radius = 25;

difference(){
    
cylinder(10,pour_radius + 7,pour_radius+ 7);
#cylinder(15,pour_radius - 5 ,pour_radius - 5);
//translate([-140,-pour_radius -5,0]) #cube([100,pour_radius * 2,20]);
    for (i = [0:8]) {
    echo(180*i/8, sin(180*i/8)*pour_radius, cos(180*i/8)*pour_radius);
    translate([sin(180*i/8)*pour_radius, cos(180*i/8)*pour_radius, 0 ])
    #cylinder(20, fuzzy_radius+shell_thickness, fuzzy_radius+shell_thickness);
}

}

translate([-50,-pour_radius,0]) cube([11,pour_radius * 2,30]);
translate([-50,-pour_radius,0]) cube([34,pour_radius * 2,10]);
