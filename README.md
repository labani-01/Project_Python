# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content. 


This is a brief outline of my project-2.

In this project we want see the distribution of N number of charged particles when they come out from the source travel through an electromagnetic region and reach the detector.

The source has some kind of symmetry and the no. of particles are different in different directions. The initial angles were drawn from a gaussian probability distribution between -pi to +pi. So the number of particles will be proportional to the total number of initial angles generated through the distribution. After coming out from the source it goes through an electromagnetic field and then reached to the circular detector placed at 1 m from the source. Due to the presence of EM field there will be shift of the charged particles in some specific directions. So the final angular distribution won't be same with the initial one. There will be shift in the gaussian distribution for the final particles. 

I have created a package named: lrpackage and the lrmonte is the python script there. In this script, I have defined a class for the Rejection sampling. And then using it from the initial_condition.py module.
Initial_condition.py module is generating initial velocities and then calling it from the main script. 
To solve the ODE of the charged particle in the electromagnetic field the main script is calling trajectory module and then storing all x and y coordinates of the N particles in single x and y array. 
Then from the main function I am putting condition to check which x and y are reaching the detector and then we are collecting these values. Using the final y and x values, we are calculating final angles and then I have shown a distribution of final angle. 
