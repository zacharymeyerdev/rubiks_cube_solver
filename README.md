# rubik's_cube_solver
a rubik's cube has 6 faces
we need a 3d array of colors and faces
    face: [[R, R, R], [R, R, R], [R, R, R]]
    cube: [[[B, B, B], [B, B, B], [B, B, B]], [[Y, Y, Y], [Y, Y, Y], [Y, Y, Y]], [[W, W, W], [W, W, W], [W, W, W]], [[G, G, G], [G, G, G], [G, G, G]], [[O, O, O], [O, O, O], [O, O, O]]]
need to be able to track and change arrays horizontally and vertically
colors: red, blue, yellow, white, green, orange

need a function to randomize a cube
visualizer?

the algorithm needs to find the least number of moves to fully complete the cube (each face has only one color)