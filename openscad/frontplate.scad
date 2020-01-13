// Wordclock faceplate with LED separator grid on the back


// ----- Part selection -----

// Leave both on "true" to render the whole assembly, to preview or to 3D print or machine as a single part.
// Set frontplate or grid to "false" to render only the other part, and make them separately.
render_frontplate = true; // front plate with letters
render_grid = true; // LED separation grid

// Set "render_grid" to "false" and "project_frontplate" to "true" to get a 2D render of the letters 
// for laser or CNC cutting the front plate.
// Warning: this triggers a "full" render, and is slow af.
project_frontplate = false; // 2D projection of the front plate



// ----- Front plate -----
width = 230; //mm
height = 230; //mm
thickness = 1.4; //mm

// Set this >0 for a solid front plate with the letters embossed into it from the outside.
// The idea here is that the full thickness blocks the light, but the letters are thin
// enough for the light to shine through.
// Leave at -0.1 instead of 0 to prevent rendering artifacts otherwise.
thickness_seethrough = -0.1; //mm

// Letters config
letters = [
    ["E","S","K","I","S","T","L","F","Ü","N","F"],
    ["Z","E","H","N","Z","W","A","N","Z","I","G"],
    ["D","R","E","I","V","I","E","R","T","E","L"],
    ["T","G","N","A","C","H","V","O","R","J","M"],
    ["H","A","L","B","X","Z","W","Ö","L","F","P"],
    ["Z","W","E","I","N","S","I","E","B","E","N"],
    ["K","D","R","E","I","R","H","F","Ü","N","F"],
    ["E","L","F","N","E","U","N","V","I","E","R"],
    ["W","A","C","H","T","Z","E","H","N","R","S"],
    ["B","S","E","C","H","S","F","M","U","H","R"]
];
letterdistance_x = 16.6; //mm
letterdistance_y = 19; //mm
fontstyle = "Consolas:style=Bold";
fontsize = 13;



// ----- Grid -----
grid_wall_thickness = 1.2; //mm
grid_wall_height = 7; //mm
grid_wall_cutout_high = 2; //mm
grid_wall_cutout_low = 1; //mm
grid_wall_cutout_width = 12; //mm




// ----- Don't change stuff below unless you know what you're doing -----

module main() {
    difference() {
        
        line_length = len(letters[0]);
        lines_count = len(letters);
        
        // Frontplate + back grid base
        union() {
            if (render_frontplate) {
                translate([0, 0, thickness/2]) cube([width, height, thickness], center = true);
            }
            
            if (render_grid) {
                grid_width = line_length * letterdistance_x + grid_wall_thickness;
                grid_height = lines_count * letterdistance_y + grid_wall_thickness;
                translate([0, 0, -grid_wall_height/2]) cube([grid_width, grid_height, grid_wall_height], center = true);
            }
        }

        // Letter + back grid cutouts
        start_x = -((line_length - 1) * letterdistance_x / 2);
        start_y = -((lines_count - 1) * letterdistance_y / 2);
        
        for (line_number = [1:lines_count]) {
            
            line_y = start_y + letterdistance_y * (line_number - 1); 
            
            for (letter_number = [1:line_length]) {
                
                letter_x = start_x + letterdistance_x * (letter_number - 1); 
                
                if (render_frontplate) {
                    letter = letters[lines_count - line_number][letter_number - 1];
                    translate([letter_x, line_y - (fontsize / 2), thickness_seethrough]) 
                        linear_extrude(thickness+1)
                        text(letter, font = fontstyle, size = fontsize, halign = "center");
                }
                    
                if (render_grid) {
                    translate([letter_x, line_y, -(grid_wall_height / 2)])
                        cube([
                            letterdistance_x - grid_wall_thickness, 
                            letterdistance_y - grid_wall_thickness, 
                            grid_wall_height + 0.1
                        ], center = true);        
                }
            }
            
            if (render_grid) {
                // extra cutouts to cover the LED strip base
                translate([0, line_y, -(grid_wall_height)])
                    cube([
                        (line_length - 1) * letterdistance_x, 
                        grid_wall_cutout_width, 
                        grid_wall_cutout_low * 2
                    ], center = true);
                
                translate([
                    (line_length/2) * letterdistance_x, 
                    line_y, 
                    -(grid_wall_height)
                ]) cube([
                    5, 
                    grid_wall_cutout_width, 
                    grid_wall_cutout_high * 2
                ], center = true);
                
                translate([
                    -(line_length/2) * letterdistance_x, 
                    line_y, 
                    -(grid_wall_height)
                ]) cube([
                    5, 
                    grid_wall_cutout_width, 
                    grid_wall_cutout_high * 2
                ], center = true);
            }
            
        }
    }
}

if (project_frontplate) {
    projection(cut = false) main();
} else {
    main();
}
