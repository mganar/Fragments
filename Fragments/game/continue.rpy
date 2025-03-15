# Stylish Continue Button
screen continue_button():
    vbox:
        xalign 0.5 yalign 0.9  # Centered horizontally, near the bottom
        spacing 10

        textbutton "Continue":
            style "continue_button"
            action Return()

# Define a nice button style
style continue_button is default:
    background "#3498db"  # Blue background
    hover_background "#2980b9"  # Darker blue when hovered
    xsize 250  # Width
    ysize 60  # Height
    
    font "DejaVuSans.ttf"  # Ensure this font is in your game folder
    
    ypadding 10
    xpadding 20
    outlines [(2, "#000000", 0, 0)]  # Black outline for contrast
    hover_outlines [(3, "#ffffff", 0, 0)]  # White outline when hovered