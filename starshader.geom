#version 330

layout (points) in;
layout (triangle_strip, max_vertices = 4) out;
in vec4 gcolor[];


out vec4 color;  
out vec2 vUv;
uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 p3d_ModelViewProjectionMatrixInverse;
uniform mat4 p3d_ViewMatrixInverse;
uniform vec3 camUp;
uniform vec3 camRight;
void build_circle(vec4 position, vec4 c, float size)
{    

    vec3 right = camRight.xyz;
    vec3 up = camUp.xyz;
    
    color = c;
    mat4 VP = p3d_ModelViewProjectionMatrix;  
    vec3 P = gl_in[0].gl_Position.xyz; //input point
    vec3 va = P - (right + up) * size; //up right point on quad facing camera
    gl_Position = VP * vec4(va, 1.0);  //back to view coordinates
    vUv = vec2(0.0, 0.0);
    EmitVertex();   //emit

    vec3 vb = P - (right - up) * size;
    gl_Position = VP * vec4(vb, 1.0);
    vUv = vec2(0.0, 1.0);
    EmitVertex();  

    vec3 vd = P + (right - up) * size;
    gl_Position = VP * vec4(vd, 1.0);
    vUv = vec2(1.0, 0.0);
    EmitVertex();  

    vec3 vc = P + (right + up) * size;
    gl_Position = VP * vec4(vc, 1.0);
    vUv = vec2(1.0, 1.0);
    EmitVertex();  

    EndPrimitive();  
}

void main() {    
    build_circle(gl_in[0].gl_Position, gcolor[0], 1 * gcolor[0].r);
}  
