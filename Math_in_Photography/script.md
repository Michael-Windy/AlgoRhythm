[TOC]

# Math in Photography

## Simplified Optical Model of a Camera

Because I'm not majoring in optics or physics. So here we'll only talk about the geometry instead of the practical engineering. Before we start, we are supposed to build an ideal model in case of the mathematical calculation.

### Lens

The use of the lens is to image the objects to the sensor. Nowadays camera lenses are very complicated. That is because the spherical lens can't focus precisely. This is called spherical aberration. Even if there's a non-spherical lens combination that could avoid spherical aberration, light beams with different frequencies have different refractive indices. So it's very difficult to build an ideal lens.

Imagine we have an ideal lens. The thickness of the lens can be ignored and the radius of the lens is infinity. Light beams that are perpendicular to the lens would focus on the focus. Light beams that point straight at the optical center wouldn't change their directions. Light beams from a point of light would focus on another point at the opposite side of the lens.

### Sensor

In many conditions, as the sensor is harder to move, the focusing process is the lens moving along the optical axis so the image would focus on the sensor. But here, to make the model simpler, we move the sensor and fix the lens. 

It can be proved that, with the same lens, no matter where the object is, as long as the distance between the object and the plane of the lens doesn't change, the distance between the plane of the lens and the image of the object doesn't change, too.

So we define the "object distance" as the distance between the object and the plane of the lens, and the "image distance" as the distance between the image and the plane of the lens.  

### Aperture

The aperture is the structure that controls the amount of light that goes into the camera. In real life, the aperture is separated from the lens so the radius of the light that is eventually shot on the sensor when going through the lens (Also known as exit pupil) is different from the actual radius of the aperture.

Here we pin the aperture on the lens so the radius of the aperture is the radius of the exit pupil.

If the focal length of the lens is $f$, and the exit pupil is $r$, then we can define the "f-number" $N$ as $\frac f{2r}$. (f over 2 r)

### Ray Transfer Matrix

If we use a vector to represent a light beam:

$$
\begin{bmatrix}
x\\ \theta
\end{bmatrix}
$$

In which $x$ is the distance between the optical center and the point that the light beam goes into the lens, $\theta$ is the tangent of the angle from the optical axis and the light beam.

There is a matrix that can transform the incident light into the emergent light.

$$
\begin{bmatrix}
A&B\\ C&D
\end{bmatrix}
\times
\begin{bmatrix}
x_1\\ \theta_1
\end{bmatrix}=
\begin{bmatrix}
x_2\\ \theta_2
\end{bmatrix}
$$

In our lens model, the only parameter of a lens is the focal length $f$. So as long as $f$ is definite, the matrix can be calculated. There are two methods to calculate the matrix of an ideal thin lens.

First, substitute the vector by the special value, and solve the equation. We choose the vectors with $x = 0$ and $\theta = 0$.

$$
\begin{bmatrix}
A&B\\ C&D
\end{bmatrix}
\times
\begin{bmatrix}
0\\ \theta
\end{bmatrix}=
\begin{bmatrix}
0\\ \theta
\end{bmatrix}\\
D\theta = \theta\\
B\theta = 0
$$
$$
\begin{bmatrix}
A&B\\ C&D
\end{bmatrix}
\times
\begin{bmatrix}
x\\ 0
\end{bmatrix}=
\begin{bmatrix}
x\\ -\frac xf
\end{bmatrix}\\
Ax = x\\
Cx = -\frac xf
$$

So the matrix of the lens is:

$$
\begin{bmatrix}
1 & 0\\
-\frac 1f & 1
\end{bmatrix}
$$

Another method is to simulate the imaging process. To simplify the calculation, let the light beam start from the point, whose object distance $d = 2f$. Obviously, the image is symmetric with the object about the optical center.

Define $r$ as the distance from the object to the optical axis. So $r = x - 2 \theta f$.

Then we just express the emergent light by $x$ and $\theta$ and solve the equations.

$$
x' = x\\
\theta' = \frac {- r - x}{2f} = \frac{\theta f - x} f = \theta - \frac xf\\
x' = Ax + B\theta\\
\theta' = Cx + D\theta
$$

Then we got the matrix too.

## Image Distance

To focus, we should calculate the image distance $D$ with the focal length $f$ and the object distance $d$.

If the object distance is $d$, and the distance from the object to the optical axis is $r$. The two special light beams are:

$$
\begin{bmatrix}
r\\0
\end{bmatrix}
\begin{bmatrix}
0\\-\frac rd
\end{bmatrix}
$$

With the matrix, we can get the emergent lights.

$$
\begin{bmatrix}
r\\-\frac rf
\end{bmatrix}
\begin{bmatrix}
0\\-\frac rd
\end{bmatrix}
$$

The intersection point of the emergent lights is the image. So there is an equation $r = D(\frac{r}{f} - \frac{r}{d})$. Therefore, $D = \frac{1}{\frac 1f - \frac 1d} = \frac{fd}{(d - f)}$.

Besides, the distance from the image to the optical axis $R$ can also calculated. Because $\frac rd = \frac RD$, so $R = \frac{rD}d$.

It can be observed that with the same lens, for $d$ bigger than $f$, a bigger $d$ is accompanied by a bigger $D$. And when the $d$ approaches to $+\infin$, $D$ approaches to $f$. When $d$ is in the range of $(0, f)$, the image drops on the same side of the lens as the object, so this situation can be ignored.

## Field of View

The field of view, (FOV), is the angular extent of sight that a sensor, a film or an eye can see.

In photography, the FOV people often discuss is the diagonal FOV. The parameters that affect the field of view are the focal length $f$, the object distance $d$ and the diagonal length of the sensor or film $2R$.

To calculate the FOV, just find the images that drop on the corners of the sensor and see where are the objects of these images. Then comes the equation:

$$
\text{FOV} = 2\arctan \frac RD = 2\arctan (\frac 1f - \frac 1d)R
$$

## Circle of confusion

If a point light is focused well, its image will be a dot. But if not, it will be blurred into a light spot. We can imagine that the light beams formed two light cones, tip to tip. When the focusing is perfectly good, the tip of the light cone just drops on the sensor. When the object was out of focus, the cone was sectioned by the film plane and left a light spot with the same shape as the aperture.

As in this model, the exit pupil is the same as the aperture,  both are round. Assume that the f-number is $f/N$. The system focuses on the object distance $d$ and the real distance between the object and the lens is $d + \delta$. And calculate the radius of the light spot.

First, the real image distance $D' = \frac {f(d + \delta)}{d + \delta - f}$. Let the difference of $D'$ and $D$ is $\Delta$.

$$
\Delta = D' - D = \frac {f(d + \delta)}{d + \delta - f} - \frac{fd}{(d - f)}\\
= f \left (\frac {d + \delta}{d + \delta - f} - \frac {d}{d - f}\right )\\
= f \left (\frac {f}{d + \delta - f} - \frac {f}{d - f}\right )\\
= f^2 \left (\frac 1{d + \delta - f} - \frac 1{d - f}\right )\\
= \frac {f^2\delta}{(f - d)(f - d - \delta)}
$$

Define the image of the point light as the circle of confusion (CoC). The radius of the CoC $a$ is:

$$
a = \left| \frac {\frac fN \Delta}{D'} \right|\\
= \left| \frac{f(d + \delta - f)f^2\delta}{Nf(d+\delta)(f - d)(f - d - \delta)} \right |\\
= \left | \frac{f^2\delta}{N(d+\delta)(d - f)} \right |\\
$$

## Depth of Field

Actually, every dot of a real object would never have the same object distance at the same time. But as long as the CoC is small enough, the blur of the whole object can still be ignorable.

Different films or sensors have different maximum permissible CoC. If the radius of the maximum permissible CoC is $C$. We can calculate the range of object distance that the image would be still sharp enough. And the length of the range is known as depth of field (DOF).

$$
a \leq C\\
\left | \frac{f^2\delta}{N(d+\delta)(d - f)} \right | \leq C\\
\frac{|\delta|}{d+\delta} \leq \frac {CN(d - f)}{f^2}\\
\begin{cases}
\frac{\delta}{d+\delta} \geq \frac {CN(f - d)}{f^2} & \delta < 0\\
\frac{\delta}{d+\delta} \leq \frac {CN(d - f)}{f^2} & \delta > 0
\end{cases}\\
\begin{cases}
\frac{d + \delta}{\delta} \leq \frac {f^2}{CN(f - d)} & \delta < 0\\
\frac{d + \delta}{\delta} \geq \frac {f^2}{CN(d - f)} & \delta > 0
\end{cases}\\
\begin{cases}
\frac{1}{\delta} \leq \frac {f^2}{CNd(f - d)} - \frac 1d & \delta < 0\\
\frac{1}{\delta} \geq \frac {f^2}{CNd(d - f)} - \frac 1d & \delta > 0
\end{cases}\\
\begin{cases}
\frac{1}{\delta} \leq \frac {f^2 + CN(d - f)}{CNd(f - d)} & \delta < 0\\
\frac{1}{\delta} \geq \frac {f^2 - CN(d - f)}{CNd(d - f)} & \delta > 0
\end{cases}\\
\begin{cases}
\delta \geq \frac {CNd(f - d)}{f^2 + CN(d - f)} & \delta < 0\\
\delta \leq \frac {CNd(d - f)}{f^2 - CN(d - f)} & \delta > 0
\end{cases}\\
$$

In this process, we can't promise that $f^2 - CN(f - d)$ is positive. Because the inverse proportional function is not monotomically increase, so at the last step, the inequality about $\frac 1\delta$ is not equivalent to the inequality about $\delta$.

To fix it, just consider the case if $f^2 - CN(f - d)$ is negative. When the right hand side is negative, left hand side is positive, so $\delta$ can be any positive number.

Then these are the nearest and the farest limits of the DOF.

$$
D_N = \frac {CNd(d - f)}{f^2 + CN(d - f)}\\
D_F = \begin{cases}
\frac {CNd(d - f)}{f^2 - CN(d - f)} & f^2 - CN(d - f) > 0\\
\infin & f^2 - CN(d - f) \leq 0\\
\end{cases}\\
\text{DOF} = 
\begin{cases}
\frac{2CNdf^2(d -f)}{f^4 - C^2N^2(d - f)^2} & f^2 - CN(d - f) > 0\\
\infin & f^2 - CN(d - f) \leq 0\\
\end{cases}\\
$$

So when you want to let more near objects are sharp enough while the infinity distant object sharp enough. You can just focus on the object distance of $\frac {f^2}{CN} + f$, the nearest distance to let $D_F$ be infinity.

Then observe the case that DOF is limited. Can be observed, $D_N \leq D_F$. To research on the relation between the DOF and other parameters. Just find the partial derivative of DOF with respect to every parameters.

$$
\text{DOF} = \frac{2CNdf^2(d -f)}{f^4 - C^2N^2(d - f)^2}\\
\frac{\partial \text{DOF}}{\partial C} = \frac{4C^2N^3df^2(d - f)^3}{(f^4 - C^2N^2(d - f)^2)^2} + \frac{2Ndf^2(d - f)}{f^4 - C^2N^2(d - f)^2} > 0\\
\frac{\partial \text{DOF}}{\partial N} = \frac{4C^3N^2df^2(d - f)^3}{(f^4 - C^2N^2(d - f)^2)^2} + \frac{2Cdf^2(d - f)}{f^4 - C^2N^2(d - f)^2} > 0\\
\frac{\partial \text{DOF}}{\partial d} = 2CNf^2 \left ( \frac{2dC^2N^2(d - f)^2}{(f^4 - C^2N^2(d - f)^2)^2} + \frac{2d - f}{f^4 - C^2N^2(d - f)^2} \right ) > 0\\
\frac{\partial \text{DOF}}{\partial f} = 2CNd \left ( -\frac{f^2(d - f)(4f^3 - C^2N^2(2f - 2d))}{(f^4 - C^2N^2(d - f)^2)^2} + \frac{2df - 3f^2}{f^4 - C^2N^2(d - f)^2} \right )\\
= \frac{2CNdf}{(f^4 - C^2N^2(d - f)^2)^2} \left ( -f(d - f)(4f^3 - C^2N^2(2f - 2d)) + (2d - 3f)(f^4 - C^2N^2(d - f)^2) \right )\\
= \frac{2CNdf}{(f^4 - C^2N^2(d - f)^2)^2} \left ( -2f(d - f)(2f^3 + C^2N^2(d - f)) + (2d - 3f)(f^4 - C^2N^2(d - f)^2) \right )\\
= \frac{2CNdf}{(f^4 - C^2N^2(d - f)^2)^2} \left ( -2f(2f^3d - 2f^4 + C^2N^2(d - f)^2) + (2d - 3f)(f^4 - C^2N^2(d - f)^2) \right )\\
= \frac{2CNdf}{(f^4 - C^2N^2(d - f)^2)^2} \left ( -2f(2f^3d - f^4) + (2d - f)(f^4 - C^2N^2(d - f)^2) \right )\\
= \frac{2CNdf(2d - f)}{(f^4 - C^2N^2(d - f)^2)^2} \left ( -f^4 - C^2N^2(d - f)^2 \right ) < 0\\
$$

So the DOF is positive related with $C$, is positive related with $N$, is positive related with $d$, is negative related with $f$.

## The Amount of Light

