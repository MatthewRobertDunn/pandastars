#version 330

// Uniform inputs
uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 p3d_ModelMatrix;
in vec2 p3d_MultiTexCoord0;

// Output to fragment shader
out vec4 pos;
out vec4 gcolor;
out vec2 vUv;

// Vertex inputs
in vec4 p3d_Vertex;
in vec4 p3d_Color;

void main() {
    gl_Position = p3d_Vertex;
    pos = gl_Position;
    gcolor = p3d_Color;
    vUv = p3d_MultiTexCoord0;
 }
