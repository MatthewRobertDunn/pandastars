 
float Kp = 2.0;         // Kp -  proportional gain
float Ki = 3.0;        // Ki -  Integral gain
float Kd = 4.0;        // Kd -  derivative gain

 PID pid = PID(0.1, 100, -100, 0.1, 0.01, 0.5);
