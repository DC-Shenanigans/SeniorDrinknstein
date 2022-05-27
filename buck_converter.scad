$fs=0.2;
$fn=250;

module buck_converter()
{
    shell_thickness = 1;
    standoff_height = 6;
    standoff_bevel_ratio = .75;
    standoff_radius = 1.50;
    standoff_inset = 2;
    
    edge_width = 4;
    edge_width_mod = edge_width * 2;

    standoff_radius_bevel = standoff_radius * standoff_bevel_ratio;

    depth = 43;
    width = 21;

    difference()
    {
            cube([width, depth, shell_thickness]);
            
            translate([edge_width, edge_width,-1])
            #cube([width - edge_width_mod, depth - edge_width_mod, 3]);
    }
    translate([width - standoff_inset, 37, 0]) 
    {
        
        cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
        cylinder(2,2,2);
    }
    translate([standoff_inset, 6, 0]) 
    {
        
        cylinder(standoff_height,standoff_radius,standoff_radius_bevel);
        cylinder(2,2,2);
    }
}

//buck_converter();