#version 330

#define TAU 6.28318530718
#define MAX_ITER 3


in vec4 pos;
in vec4 color;
in vec2 vUv;

out vec4 fragColor;
void main () 
{
	//fragColor = vec4(color.rgb, 1.0);
	//return;
	
	vec2 v = vUv + vec2(-0.5, -0.5);
	float l = length(v);

	if(l < 0.2){
		fragColor = vec4(color.rgb, 1.0) * (1.0 - pow(l*5.0, 4.5));
	} else {
		discard;
	}
}
