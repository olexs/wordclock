// Wordclock faceplate with LED separator grid on the back


// ----- Config -----

// Frontplate config
width = 230; //mm
height = 230; //mm
thickness = 1.4; //mm
thickness_seethrough = 0.2; //mm

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

// Back grid config
grid_wall_thickness = 1.2; //mm
grid_wall_height = 5; //mm


// ----- Construction -----

line_length = len(letters[0]);
lines_count = len(letters);
    
difference() {
    // Frontplate + back grid base
    union() {
        translate([0, 0, thickness/2]) cube([width, height, thickness], center = true);
        
        grid_width = line_length * letterdistance_x + grid_wall_thickness;
        grid_height = lines_count * letterdistance_y + grid_wall_thickness;
        translate([0, 0, -grid_wall_height/2]) cube([grid_width, grid_height, grid_wall_height], center = true);
    }

    // Letter + back grid cutouts
    start_x = -((line_length - 1) * letterdistance_x / 2);
    start_y = -((lines_count - 1) * letterdistance_y / 2);
    
    for (line_number = [1:lines_count]) {
        
        line_y = start_y + letterdistance_y * (line_number - 1); 
        
        for (letter_number = [1:line_length]) {
            
            letter_x = start_x + letterdistance_x * (letter_number - 1); 
            letter = letters[lines_count - line_number][letter_number - 1];
            
            translate([letter_x, line_y - (fontsize / 2), thickness_seethrough]) 
                linear_extrude(thickness+1)
                text(letter, font = fontstyle, size = fontsize, halign = "center");
            
            translate([letter_x, line_y, -(grid_wall_height / 2)])
                cube([
                    letterdistance_x - grid_wall_thickness, 
                    letterdistance_y - grid_wall_thickness, 
                    grid_wall_height + 0.1
                ], center = true);        
        }
    }
}