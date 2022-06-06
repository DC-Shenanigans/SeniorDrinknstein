
module buck_converter(shell_thickness=1)
{
    //shell_thickness = 1;
    //standoff_height = 6;
    standoff_bevel_ratio = .75;
    standoff_radius = 1.50;
    standoff_inset = 2;
    safety_standoff_height = 10;
    safety_standoff_radius = 2.8;

    standoff_height = 4 + safety_standoff_height;
    safety_standoff_radius = 2.5;
    edge_width = 4;
    edge_width_mod = edge_width * 2;

    standoff_radius_bevel = standoff_radius * standoff_bevel_ratio;

    depth = 43;
    width = 21;

    difference()
    {
            cube([width, depth, shell_thickness]);
            
            translate([edge_width, edge_width,-1])
            #cube([width - edge_width_mod, depth - edge_width_mod, shell_thickness + 10]);
    }
    difference(){
        translate([width - standoff_inset, 37, shell_thickness]) 
        {
        cylinder(safety_standoff_height,safety_standoff_radius,safety_standoff_radius);
        }
        translate([width - standoff_inset, 37, shell_thickness]) 
        {
            #cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
        }
    }
    difference(){
        translate([standoff_inset, 6, shell_thickness]) 
        {
        cylinder(safety_standoff_height,safety_standoff_radius,safety_standoff_radius);
        }
        translate([standoff_inset, 6, shell_thickness]) 
        {
            
            #cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
        }
    }
}

//buck_converter();